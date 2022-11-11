from django.shortcuts import render, redirect, get_object_or_404
from .forms import CashbookForm, CommentForm, HashtagForm
from django.utils import timezone
from .models import Cashbook, Comment, Hashtag
from account.models import CustomUser
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from account.loginmessage import *
from django.db.models import Q


# Create your views here.

def main(request):
    return render(request, 'main.html')
 

@login_message_required
def write(request, cashbook = None):
    if request.method == 'POST':
        form = CashbookForm(request.POST, request.FILES, instance = cashbook)
        if form.is_valid():
            author = request.user
            cashbook = form.save(commit = False)
            cashbook.author = request.user
            cashbook.save()
            content = request.POST.get('content')
            content_list = content.split(' ')
            form.save_m2m()
            for c in content_list:
                if '#' in c:
                    hashtag = Hashtag()
                    hashtag.hashtag_content = c
                    cashbook_ = Cashbook.objects.get(id = cashbook.id)
                    cashbook_.tagging.add(hashtag)
            return redirect('/')
        else:
            return redirect('write', {'author':author})
    else:
        form = CashbookForm(instance = cashbook)
        return render(request, 'write.html', {'form':form})

def read(request):
    sort = request.GET.get('sort', '')
    if sort == 'date':
        cashbooks = Cashbook.objects.all().order_by('-date')
    elif sort == 'like_count':
        cashbooks = Cashbook.objects.all().order_by('-like_count')
    else:
        cashbooks = Cashbook.objects
    return render(request, 'read.html', {'cashbooks':cashbooks, 'sort': sort})

def edit(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.method == "POST":
        form = CashbookForm(request.POST, request.FILES, instance=cashbooks)
        if form.is_valid():
            form.save(commit=False)
            form.updated_at = timezone.now()
            form.save()
            return redirect('read')

    else:
        form = CashbookForm(instance=cashbooks)
        return render(request, 'edit.html', {'form':form, 'cashbooks':cashbooks})

def delete(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    cashbooks.delete()
    return redirect('read')

def detail(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.cashbook_id = cashbooks
            comment.author = request.user
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail', cashbooks.id)
    else:
        form = CommentForm()
        forms = Comment.objects.filter(id=id)
        return render(request, 'detail.html', {'cashbooks': cashbooks, 'form':form})


def update_comment(request, id, com_id):
    post = get_object_or_404(Cashbook, id=id)
    comment = get_object_or_404(Comment, id=com_id)
    form = CommentForm(instance=comment)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance = comment)
        if update_form.is_valid():
            update_form.save()
            return redirect('detail', id)
    return render(request, 'update_comment.html', {'form':form, 'post':post, 'comment':comment})


def delete_comment(request, id, com_id):
    comment = get_object_or_404(Comment, id=com_id)
    comment.delete()
    return redirect('detail',id)


def hashtag(request, hashtag = None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance = hashtag)
        if form.is_valid():
            hashtag = form.save(commit = False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = '이미 존재하는 해시태그입니다.'
                return render(request, 'hashtag.html', {'form':form, 'error_message': error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('read')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'hashtag.html',{'form':form})


def hashtag_home(request):
    hashtags = Hashtag.objects.all()
    return render(request, 'hashtag_home.html', {'hashtags':hashtags})

def hashtag_detail(request, id, hashtag_id):
    hashtags = get_object_or_404(Hashtag, id=id)
    hashtag = Hashtag.objects.filter(name=hashtags)
    hashtag_posts = Cashbook.objects.filter(hashtags__in = hashtag)
    return render(request, 'hashtag_detail.html', {'hashtag':hashtag, 'hashtag_posts':hashtag_posts})
   
def hashtag_delete(request, id, hashtag_id):
    cashbook = get_object_or_404(Cashbook, id=id)
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    cashbook.hashtags.remove(hashtag)
    if hashtag.cashbook_set.count() == 0:
        hashtag.delete()
    return redirect('detail', id=id)

@login_message_required
def like(request, id):
    like_b = get_object_or_404(Cashbook, id=id)
    if request.user in like_b.post_like.all():
        like_b.post_like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.post_like.add(request.user)
        like_b.like_count += 1
        like_b.save()
    return redirect('detail', like_b.id)


def search(request):
    cashbooks = Cashbook.objects.all()
    search = request.GET.get('search', '')
    if search:
        cashbooks = cashbooks.filter (
            Q(title__icontains = search) | # 제목
            Q(content__icontains = search)  # 내용
        ).distinct()
        return render(request, 'search.html', {'cashbooks':cashbooks, 'search':search})
    else:
        return render(request, 'search.html')


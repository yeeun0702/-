from django.shortcuts import render, redirect, get_object_or_404
from .forms import CashbookForm, CommentForm
from django.utils import timezone
from .models import Cashbook, Comment
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from account.loginmessage import *

# Create your views here.

def main(request):
    return render(request, 'main.html')
 

@login_message_required
def write(request):
    context = {}
    if request.method == 'POST':
        form = CashbookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_at = timezone.now()
            form.author = request.user
            form.save()
            return redirect('detail',form.id)

        else:
            context = {
                'form':form,
            }
            return render(request, 'write.html', context)

        
    else:
        form = CashbookForm
        return render(request, 'write.html', {'form':form})
        

def read(request):
    cashbooks = Cashbook.objects.all()
    return render(request, 'read.html', {'cashbooks':cashbooks})

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
from django.contrib import admin
from django.urls import path
import cashbookapp.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import URLPattern, path
from cashbookapp import views
import cashbookapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cashbookapp.views.main, name='main'),
    path('write/', cashbookapp.views.write, name='write'),
    path('read/', cashbookapp.views.read, name='read'),
    path('detail/<str:id>', cashbookapp.views.detail, name='detail'),
    path('edit/<str:id>', cashbookapp.views.edit, name='edit'),
    path('delete/<str:id>', cashbookapp.views.delete, name='delete'),
    path('update_comment/<str:id>/<str:com_id>/', cashbookapp.views.update_comment, name='update_comment'),
    path('delete_comment/<str:id>/<str:com_id>/', cashbookapp.views.delete_comment, name='delete_comment'),
    path('hashtag/', cashbookapp.views.hashtag, name='hashtag'),
    path('hashtag_home/', cashbookapp.views.hashtag_home, name="hashtag_home"),
    path('hashtag_detail/<str:id>/<str:hashtag_id>/', cashbookapp.views.hashtag_detail, name="hashtag_detail"),
    path('hashtag_delete/<str:id>/hashtag/<str:hashtag_id>/delete', cashbookapp.views.hashtag_delete, name="hashtag_delete"),
    path('search/', cashbookapp.views.search, name='search'),
    path('like/<str:id>/', cashbookapp.views.like, name='like')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
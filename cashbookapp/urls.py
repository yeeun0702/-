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
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
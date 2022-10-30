from django.urls import URLPattern, path
from account import views
from django.conf import settings
from django.conf.urls.static import static
import account.views

urlpatterns = [
    path('signup/',account.views.signup, name= 'signup'),
    path('login/',account.views.login, name= 'login'),
    path('logout/',account.views.logout, name= 'logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage_edit/', views.mypage_edit, name='mypage_edit'),
    path('update_password/',account.views.update_password, name='update_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
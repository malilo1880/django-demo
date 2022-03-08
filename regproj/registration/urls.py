from registration import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('display/',views.display,name='display'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
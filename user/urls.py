from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('<int:pk>/', views.newspaper, name='newspaper'),
    path('<int:pk>/subscription', views.subscription, name='subscription'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

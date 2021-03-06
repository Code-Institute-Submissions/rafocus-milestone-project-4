from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls') ),
    path('', include('carts.urls') ),
    path('', include('checkout.urls') ),
    path('', include('contact.urls') ),
    path('register/', user_views.register, name='register'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

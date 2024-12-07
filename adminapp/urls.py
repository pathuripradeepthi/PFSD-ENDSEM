from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('Login/',views.Login,name='Login'),
    path('Register/',views.Register,name='Register'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLogicPageCall'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('dashboard/', views.dashboard, name='dashboard'),

]

from django.urls import path
from account import views


urlpatterns = [    
    path('register/',views.UserRegistrationView.as_view(),name='register'),
    path('verify/', views.UserVerificationView.as_view(), name='user-verification'),
    path('reverify/', views.ReUserVerificationView.as_view(), name='reuser-verification'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('profile/',views.UserProfileView.as_view(),name='profile'),
    path('changepassword/',views.UserChangePassword.as_view(),name='changepassword'),
    path('send-reset-password-email/',views.SendPasswordResetEmailView.as_view(),name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',views.UserpasswordResetView.as_view(),name='reset-password'),
]
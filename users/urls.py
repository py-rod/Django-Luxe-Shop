from django.urls import path
from . import views


urlpatterns = [
    path('account/signup', views.signup, name='signup'),
    path("account/users/activate/<uidb64>/<token>",
         views.activate, name="activate"),
    path('account/signin', views.signin, name='signin'),

    # GOOGLE
    path("social/signup/", views.redirect_signin_with_google, name="signup_redirect"),
    path("social/login/cancelled/", views.redirect_signin_whith_google_cancel,
         name="signin_cancel_redirect"),

    path('3rdparty/signup/',
         views.redirect_signin_with_google_3rdparty, name='signup_3rdparty_redirect'),
    path('3rdparty/login/cancelled/', views.redirect_signin_with_google_cancel_3rdparty,
         name='signin_cancel_3rdparty_cancel')
]

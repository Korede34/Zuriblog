from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from blog.views import SignupView
from django.contrib.auth.views import (
                                    LoginView,
                                    LogoutView,
                                    PasswordResetView, 
                                    PasswordResetDoneView, 
                                    PasswordResetConfirmView, 
                                    PasswordResetCompleteView
                                )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

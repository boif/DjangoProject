from datetime import datetime
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Profile import views, forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',
         LoginView.as_view
             (
             template_name='registration/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
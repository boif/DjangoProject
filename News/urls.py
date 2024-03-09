from django.urls import path
from News import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.createPost, name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
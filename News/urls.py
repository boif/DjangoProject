from django.urls import path
from News import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.createPost, name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
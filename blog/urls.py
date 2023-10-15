from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, MaterialDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs_homepage'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/<str:slug>', MaterialDetailView.as_view(), name='view'),
    path('edit/<int:pk>/<str:slug>', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/<str:slug>', BlogDeleteView.as_view(), name='delete'),
]
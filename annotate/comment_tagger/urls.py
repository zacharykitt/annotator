from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='comments.index'),
    path('complete/<int:comment_id>/', views.complete, name='comments.complete'),
    path('create_tag/<int:comment_id>/', views.create_tag, name='comments.create_tag'),
    path('tag/<int:comment_id>/<int:tag_id>/', views.tag, name='comments.tag'),
    path('remove/<int:comment_id>/<int:tag_id>/', views.remove, name='comments.remove'),
    path('view/<int:comment_id>/', views.select, name='comments.select'),
    path('prev/<int:comment_id>/', views.prev, name='comments.prev'),
    path('next/<int:comment_id>/', views.next, name='comments.next'),
]
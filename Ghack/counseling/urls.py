from django.urls import path
from . import views

urlpatterns = [
    path('counseling/', views.counseling, name='counseling'),

    #-----------------Posts-----------------#
    path('posts/', views.get_posts, name='get_posts'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('upvote_post/<int:post_id>/', views.upvote_post, name='upvote_post'),
    path('downvote_post/<int:post_id>/', views.downvote_post, name='downvote_post'),

    #-----------------Comments-----------------#
    path('comments/<int:post_id>/', views.get_comments, name='get_comments'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('upvote_comment/<int:comment_id>/', views.upvote_comment, name='upvote_comment'),
    path('downvote_comment/<int:comment_id>/', views.downvote_comment, name='downvote_comment'),
    
]

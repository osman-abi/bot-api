from django.urls import path
from .views import ContactAPI, DetailContactAPI, PostListAPI, PostDetailAPI, SendMessageCommentAuthor, ReplyMessageAPI, ReplyMessageEditAPI




urlpatterns = [
    path('posts/', PostListAPI.as_view()),
    path('posts/<str:post_id>/', PostDetailAPI.as_view()),

    path('send-message-comment-author/<str:comment_id>', SendMessageCommentAuthor.as_view()),

    path('contacts/', ContactAPI.as_view()),
    path('contacts-detail/<int:pk>', DetailContactAPI.as_view()),

    path('reply-message/', ReplyMessageAPI.as_view()),
    path('reply-message-edit/<int:pk>/', ReplyMessageEditAPI.as_view())
]
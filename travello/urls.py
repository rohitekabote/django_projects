from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('description/<int:id>/', views.description, name='description'),
    path('comment/<int:comment_id>/<str:action>/', views.like_dislike_comment, name='like_dislike_comment'),

]
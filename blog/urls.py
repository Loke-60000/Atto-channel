from django.urls import path
from . import views

urlpatterns = [

    path('threads/', views.ShowNewsView.as_view(), name='home-page'),
    path('comment/<int:pk>', views.NewsDetailView.as_view(), name='comment-detail'),
    path('comment/<int:pk>/update', views.UpdateNewsView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete', views.DeleteNewsView.as_view(), name='comment-delete'),
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user-comment'),


    #to change/check!
    path('threads/<int:pk>/add', views.CreateNewsView.as_view(), name='comment-add'),
    path('threads/<int:pk>', views.ThreadsDetailView.as_view(), name='threads-detail'),
    path('', views.ShowThreadsView.as_view(), name='threads'),
    path('about', views.contacti, name='contacti'),
]


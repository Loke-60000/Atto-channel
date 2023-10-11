from django.urls import path
from . import views

urlpatterns = [

    path('', views.ShowNewsView.as_view(), name='home-page'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user-news'),


    #to change/check!
    path('threads/<int:pk>/add', views.CreateNewsView.as_view(), name='comment-add'),
    path('threads/<int:pk>', views.ThreadsDetailView.as_view(), name='threads-detail'),
    path('threads/', views.ShowThreadsView.as_view(), name='threads'),
    path('conversations', views.contacti, name='conversations'),
    path('about', views.contacti, name='contacti'),

]


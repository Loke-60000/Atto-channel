from django.urls import path
from . import views

urlpatterns = [

    path('threads/', views.ShowPostsView.as_view(), name='home-page'),
    path('comment/<int:pk>', views.PostDetailView.as_view(), name='comment-detail'),
    # path('comment/<int:pk>/delete', views.DeletePostView.as_view(), name='comment-delete'),
    path('user/<str:username>', views.UserAllPostsView.as_view(), name='user-comment'),

    path('threads/<int:pk>/add', views.CreatePostView.as_view(), name='comment-add'),
    path('threads/<int:pk>', views.ThreadsDetailView.as_view(), name='threads-detail'),
    path('', views.ShowThreadsView.as_view(), name='threads'),
    path('about', views.about, name='contacti'),
    path('comment/<int:pk>/reply', views.CreateRepliesView.as_view(), name='comment-reply'),

    #temp
    path('404/', views.get404, name='get404'),
    path('500/', views.get500, name='get500'),
    path('set/', views.SetSession, name='set'),
    path('get/', views.GetSession, name='get'),
]

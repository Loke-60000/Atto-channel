import time

from django.shortcuts import (
    get_list_or_404
)
from django.contrib.auth.models import User, AnonymousUser


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import News, Threads, Replies
from django.shortcuts import render
import hashlib
from PIL import Image

def SetSession(request):
    #user id based on current time with hash
    user_id = hashlib.sha256(f"{time.time()}".encode('utf-8')).hexdigest()[:9]
    request.session['user_id'] = user_id

def GetSession(request):
    user_id = request.session.get('user_id')
    return user_id

class ShowPostsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5
    def get_context_data(self, **kwargs):
        ctx = super(ShowPostsView, self).get_context_data(**kwargs)
        ctx['title'] = 'All comments. Search thread/1,2,3.. to view threads.'

        return ctx


#implenment new profile base for @chan users! For test purposes base.html is used. PS. 4nmus
class UserAllPostsView(ListView):
    model = News
    template_name = 'blog/comments_user.html'
    context_object_name = 'news'
    #change later to 5 approximately! PS. Your 4nmus
    paginate_by = 5

    def get_queryset(self):
        user = get_list_or_404(User, username=self.kwargs['username'])[0]
        return News.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserAllPostsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Author page'
        return ctx

class PostDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwards):
        ctx = super(PostDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-comment.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class CreatePostView(CreateView):
    model = News
    template_name = 'blog/create_comment.html'
    context_object_name = 'news'
    fields = ['text', 'img']

    def get_context_data(self, **kwards):
        ctx = super(CreatePostView, self).get_context_data(**kwards)
        ctx['title'] = 'Add post'
        ctx['btn_text'] = 'Add'
        return ctx

    def form_valid(self, form):
        
        #temporary
        if not isinstance(self.request.user, AnonymousUser):
            form.instance.author = self.request.user
            # user for unique id
            form.instance.rand_id = hashlib.sha256(f"{self.request.user}".encode('utf-8')).hexdigest()[:9]
        else:
            if GetSession(self.request) is None:
                SetSession(self.request)
            form.instance.rand_id = hashlib.sha256(GetSession(self.request).encode('utf-8')).hexdigest()[:9]

        current_thread = Threads.objects.get(pk=self.kwargs['pk'])
        form.instance.thread = current_thread
        return super().form_valid(form)


class ShowThreadsView(ListView):
    model = Threads
    template_name = 'blog/main-extended.html'
    context_object_name = 'threads'
    paginate_by = 4
    ordering = ['date']
    def get_context_data(self, **kwargs):
        ctx = super(ShowThreadsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Popular threads!'

        # implement shuffle ? Subject to change. Ps 4nmus
        ctx['threads'] = Threads.objects.all()

        return ctx




class ThreadsDetailView(TemplateView):
    model = Threads
    template_name = 'blog/thread.html'
    context_object_name = 'post'

    def get_context_data(self, **kwards):
        ctx = super(ThreadsDetailView, self).get_context_data(**kwards)
        current_thread = Threads.objects.get(pk=self.kwargs['pk'])
        ctx['title'] = current_thread
        ctx['news'] = News.objects.filter(thread=current_thread).order_by('-date')
        ctx['replies'] = Replies.objects.filter(thread=current_thread)
        return ctx

class CreateRepliesView(CreateView):
    model = Replies
    template_name = 'blog/create_comment.html'
    context_object_name = 'replies'
    fields = ['text']
    def get_context_data(self, **kwards):
        ctx = super(CreateRepliesView, self).get_context_data(**kwards)
        ctx['title'] = 'Add reply'
        ctx['btn_text'] = 'Add'
        return ctx

    def form_valid(self, form):
        if not isinstance(self.request.user, AnonymousUser):
            form.instance.author = self.request.user
            form.instance.rand_id = hashlib.sha256(f"{self.request.user}".encode('utf-8')).hexdigest()[:9]
        current_comment = News.objects.get(pk=self.kwargs['pk'])
        form.instance.original = current_comment
        form.instance.thread = current_comment.thread
        return super().form_valid(form)

# change!
def about(request):
    return render(request, 'blog/about.html')

def get404(request):
    return render(request, 'blog/404.html')
def get500(request):
    return render(request, 'blog/500.html')
# Create your views here.

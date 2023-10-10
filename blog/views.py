from django.shortcuts import (
    render,
    get_list_or_404
)
from django.contrib.auth.models import User, AnonymousUser
from .models import News

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import News, Threads
from django.shortcuts import render, get_object_or_404

class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5
    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'All comments. Search thread/1,2,3.. to view threads.'

        return ctx


#implenment new profile base for @chan users! For test purposes base.html is used. PS. 4nmus
class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/news_user.html'
    context_object_name = 'news'
    #change later to 5 approximately! PS. Your 4nmus
    paginate_by = 5

    def get_queryset(self):
        user = get_list_or_404(User, username=self.kwargs['username'])[0]
        return News.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserAllNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Author page'
        return ctx

class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Update article'
        ctx['btn_text'] = 'Update'
        return ctx


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False

# temp decision for implementing anon users
# LoginRequiredMixin


class CreateNewsView(CreateView):
    model = News
    template_name = 'blog/create_news.html'
    context_object_name = 'news'
    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Add comment'
        ctx['btn_text'] = 'Add'
        return ctx

    def form_valid(self, form):
        # temp decision for implementing anon users
        if not isinstance(self.request.user, AnonymousUser):
            form.instance.author = self.request.user
        current_thread = Threads.objects.get(pk=self.kwargs['pk'])
        form.instance.thread = current_thread

        return super().form_valid(form)


class ShowThreadsView(ListView):
    model = Threads
    template_name = 'blog/main.html'
    context_object_name = 'threads'

    def get_context_data(self, **kwargs):
        ctx = super(ShowThreadsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Popular threads!'
        return ctx


#For testing! Change to ↑↑↑ later! Ps. 4nmus
def threads(request):
    data = {
        'threads': Threads.objects.all(),
        'title': 'Popular threads!'
    }
    return render(request, 'blog/main.html', data)


class ThreadsDetailView(TemplateView):
    model = Threads
    # to change!
    template_name = 'blog/thread.html'
    context_object_name = 'post'

    def get_context_data(self, **kwards):
        ctx = super(ThreadsDetailView, self).get_context_data(**kwards)
        current_thread = Threads.objects.get(pk=self.kwargs['pk'])
        ctx['title'] = current_thread
        ctx['news'] = News.objects.filter(thread=current_thread).order_by('-date')
        return ctx


# change!
def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Just a page!'})

# Create your views here.




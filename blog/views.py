from django.shortcuts import render
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Main!'
    }
    return render(request, 'blog/home.html', data)


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Main paage!!!'
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
    pass


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    pass

class CreateNewsView(LoginRequiredMixin, CreateView):
    pass

def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Just a page!'})

# Create your views here.

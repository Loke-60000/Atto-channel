from django.contrib import admin
from .models import News, Threads, Replies

admin.site.register(News)
admin.site.register(Threads)
admin.site.register(Replies)

# Register your models here.

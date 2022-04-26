from django.shortcuts import render, redirect
from django.views import View

from .models import Blog, Category, Tag
from .forms import BlogForm, CommentForm


class BaseView:
    def category(self):
        category_list = Category.objects.all()
        return category_list

    def tag(self):
        tag_list = Tag.objects.all()
        return tag_list


class BlogList(BaseView, View):
    def get(self, request):
        context = {}
        context['blogs'] = Blog.objects.all()
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'blog_list.html', context)


class BlogByCategory(BaseView, View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        blogs = Blog.objects.filter(category=category)
        categories = self.category()
        tags = self.tag()
        context = {
            'blogs': blogs,
            'category': category,
            'categories': categories,
            'tags': tags,
        }

        return render(request, 'category_blogs.html', context)


class BlogCreate(BaseView, View):
    def get(self, request):
        context = {}
        context['form'] = BlogForm()
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'blog_create.html', context)

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')


class BlogDetail(BaseView, View):
    def get(self, request, slug):
        context = {}
        blog = Blog.objects.get(slug=slug)
        context['blog'] = blog
        context['categories'] = self.category()
        context['tags'] = self.tag()
        context['form'] = CommentForm()

        blog.views += 1
        blog.save()

        return render(request, 'blog_detail.html', context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form_comment = form.save(commit=False)
            form_comment.blog = Blog.objects.get(slug=slug)
            form_comment.user = request.user
            form_comment.save()
            return redirect('blog_detail', form_comment.blog.slug)
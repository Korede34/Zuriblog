from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Post
from .forms import UserCreation, PostForm, CommentForm
from django.views import generic


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreation
    
    def get_success_url(self):
        return reverse('login')


class PostListView(generic.ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()


class PostDetailView(generic.edit.FormMixin, generic.DetailView):
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
    form_class = CommentForm
    queryset = Post.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = self.object
        comment.save()
        return super(PostDetailView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('post-list')


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'blog/post-create.html'
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})
            
    def form_valid(self, form):
        author = self.request.user.author
        post = form.save(commit=False)
        post.author = author
        post.save()
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'blog/post-update.html'
    form_class = PostForm
    queryset = Post.objects.all()

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'blog/post-delete.html'
    queryset = Post.objects.all()
    
    def get_success_url(self):
        return reverse('post-list')
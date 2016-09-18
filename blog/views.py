from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, CreateView
# --------------------------------------------------------------------------------------
from blog.models import Post
from .forms import PostForm


class PostsListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)
        success_url = "/login/"

        template_name = "register.html"

        def form_valid(self, form):
            form.save()

            return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect("/")

class LoggedInMixin(object):
        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class PostOwnerMixin(object):
    def get_object(self, queryset=None): 
        if queryset is None: 
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None) 
        queryset = queryset.filter(
            pk=pk, 
            owner=self.request.user, 
        )
        try:
            obj = queryset.get() 
        except ObjectDoesNotExist: 
            raise PermissionDenied
        return obj

class OwnerPostsListView(LoggedInMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class OwnerPostDetailView(LoggedInMixin, PostOwnerMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def post_new(request):
        if request.method == "POST":
             form = PostForm(request.POST)
             if form.is_valid():
                post = form.save(commit=False)
                post.owner = request.user
                post.published_date = timezone.now()
                post.save()
                return HttpResponseRedirect(reverse("post_detail", kwargs={"pk": post.pk}))
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
             form = PostForm(request.POST, instance=post)
             if form.is_valid():
                post = form.save(commit=False)
                post.owner = request.user
                post.published_date = timezone.now()
                post.save() 
                return HttpResponseRedirect(reverse("post_detail", kwargs={"pk": post.pk}))
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

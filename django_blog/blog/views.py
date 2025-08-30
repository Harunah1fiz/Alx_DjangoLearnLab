from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegistration,UserUpdateForm,ProfileUpdateForm,PostForm, CommentForm
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Profile, Post, Comment
from django.shortcuts import get_object_or_404
#blog comments



# Create your views here.
#registration
def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account has been Created")
            return redirect("login")
    else:
        form = UserRegistration()
    return render(request, "accounts/register.html", {"form": form})


def prof(request):
    return render(request, "accounts/profile.html")
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        print(f" user : {u_form.errors}, profile : {p_form.errors}")
        if u_form.is_valid() and p_form.is_valid():
            print("checked")
            u_form.save()
            p_form.save()
            return redirect('login')
    else:
        print("not checked")
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "accounts/profile.html", {'u_form': u_form, 'p_form':p_form})

def betterRegister(request):
        if request.method == "POST":
            form = UserRegistration(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, "Your account has been Created")
                return redirect("login")
        else:
            form = UserRegistration()
        return render(request, "accounts/register.html", {"form": form})

#blogs

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to update an existing blog post.
    - Only the author of the post can update it.
    - The form automatically sets the author to the current logged-in user.
    """

    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")
    context_object_name = "post"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author 

    def handle_no_permission(self):
        return redirect("post_list")
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    


#comment


# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form_class = CommentForm

#     def form_valid(self, form):
#         post = get_object_or_404(post, pk=self.kwargs['pk'])
#         form.instance.post = post
#         form.instance.author = self.request.user
#         return super().form_valid(form)
    

#     def get_success_url(self):
#         return self.object.post.get_absolute_url()
def CommentCreateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post.pk)

    return redirect("post_detail", pk = post.pk)

        


    

#update ccomment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView)
from blog_app.models import Post, Comment
from blog_app.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required  #for Function based Views
from django.contrib.auth.mixins import LoginRequiredMixin  #for Class based Views

# Create your views here.

class AboutView(TemplateView):
    
    #customize page name
    template_name="about.html"


class PostListView(ListView):
    
    model = Post
    
    #defining a custom object to return, otherwise it returns "school"s_list (schools_list)
    #class model attribute hardcoded
    context_object_name = "post_list"  #this is used in HTML   
        
    #CUSTOM query return ORM
    def get_queryset(self):
        
        #  __lte  ORM attribution to Class field
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
        #return Post.objects.all()
    
    
class PostDetailView(DetailView):
    model=Post
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    
    #Using decorators to define security per user role    
    login_url = "/login/"
    redirect_field_name = "blog_app/post_detail.html"
    
    form_class = PostForm
    
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model=Post
    
     #Using decorators to define security per user role    
    login_url = "/login/"
    redirect_field_name = "blog_app/post_detail.html"
    
    form_class = PostForm   
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model=Post
    
    #Customizes template name for the class method
    template_name = "blog_app/post_confirm_delete.html"
    
    #Udelete is successful, goes to 
    success_url = reverse_lazy("blog_app:post_list_url")
    
    
class DraftListView(LoginRequiredMixin,ListView):
    model = Post
    
    login_url = "/login/"
    redirect_field_name = "blog_app/post_list.html"
    
    #CUSTOM query return ORM - No date published
    def get_queryset(self):
        
        #  __lte  ORM attribution to Class field
        return Post.objects.filter(published_date__isnull=True).order_by("create_date")
       

############################################################################################


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("blog_app:post_detail_url", pk=pk)
    

@login_required   # Decorator from django.contrib.auth.decorators
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("blog_app:post_detail_url", pk=post.pk)
    else:
        form = CommentForm()
    
    context_return = {"form":form}
    
    return render(request,"blog_app/comment_form.html",context_return)


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    # PK is identifiable same as pk=comment.post.post_id
    return redirect("blog_app:post_detail_url",pk=comment.post.pk)
    
@login_required
def  comment_remove(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    prev_post_pk = comment.post.pk
    
    comment.delete()
    
    return redirect("blog_app:post_detail_url",pk=prev_post_pk)










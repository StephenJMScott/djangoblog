from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, BlogCommentForm
from django.utils import timezone

# Create your views here.

def get_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render (request, "posts.html", {'posts':posts})
    
    
def viewpost(request, id):
    this_post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post=this_post)
    form= BlogCommentForm()

    return render(request, "postdetail.html", {'post': this_post, 'comments': comments, 'form':form })
    
@login_required()
def newpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(viewpost, post.pk)
    else:
        form=BlogPostForm()
    return render(request, 'postform.html', {'form':form})
    

@login_required()
def editpost(request, id):
    post=get_object_or_404(Post, pk=id)
    if request.method =='POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(viewpost, post.pk)
    else:
        form=BlogPostForm(instance=post)
    return render(request, 'postform.html', {'form':form})
        
@login_required()
def deletepost(request, id):
    post=get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('home')
    


@login_required()
def addcomment(request, post_id):
    post= get_object_or_404(Post, pk=post_id)
    
    form = BlogCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        
        comment.save()
        
        return redirect('viewpost', post_id)

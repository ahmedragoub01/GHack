from django.shortcuts import render
from .models import Post , Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def counseling(request):
    return render(request, 'counseling.html')


#-----------------Posts-----------------#

def get_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        #sort by score
        posts = sorted(posts, key=lambda x: x.score, reverse=True)

        return render(request, 'posts.html', {'posts': posts})
    
@login_required
def add_post(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        body = request.POST['body']
        post = Post(title=title, body=body)
        post.save()
        return render(request, 'posts.html', {'posts': Post.objects.all()})
    
def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(post_id=post_id)
        
        # Check if the post belongs to the current user
        if post.user != request.user:
            return HttpResponseForbidden("You are not allowed to delete this post.")
        
        post.delete()
        return render(request, 'posts.html', {'posts': Post.objects.all()})
    
    
@login_required
def upvote_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(post_id=post_id)
        
        # Check if the user has already upvoted the post
        if post.upvotes.filter(id=request.user.id).exists():
            return HttpResponseForbidden("You have already upvoted this post.")
        
        # Check if the user has already downvoted the post
        if post.downvotes.filter(id=request.user.id).exists():
            post.downvotes.remove(request.user)
            post.score += 1
        
        post.upvotes.add(request.user)
        post.score += 1
        post.save()
        return render(request, 'posts.html', {'posts': Post.objects.all()})

@login_required
def downvote_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(post_id=post_id)
        
        # Check if the user has already downvoted the post
        if post.downvotes.filter(id=request.user.id).exists():
            return HttpResponseForbidden("You have already downvoted this post.")
        
        # Check if the user has already upvoted the post
        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
            post.score -= 1
        
        post.downvotes.add(request.user)
        post.score -= 1
        post.save()
        return render(request, 'posts.html', {'posts': Post.objects.all()})
    
#-----------------Comments-----------------#
    
def get_comments(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(post_id=post_id)
        comments = Comment.objects.filter(post=post)
        return render(request, 'comments.html', {'post': post, 'comments': comments})
    
@login_required
def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        user = request.user
        post = Post.objects.get(post_id=post_id)
        body = request.POST['body']
        rating = request.POST['rating']
        comment = Comment(user=user, post=post, body=body, rating=rating)
        comment.save()
        comments = Comment.objects.filter(post=post)
        return render(request, 'comments.html', {'post': post, 'comments': comments})
    
@login_required
def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(Comment_id=comment_id)
        
        # Check if the current user is the owner of the comment
        if comment.user != request.user:
            return HttpResponseForbidden("You are not authorized to delete this comment.")
        
        post = comment.post
        comment.delete()
        comments = Comment.objects.filter(post=post)
        return render(request, 'comments.html', {'post': post, 'comments': comments})
    
@login_required
def upvote_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(Comment_id=comment_id)
        
        # Check if the user has already upvoted the comment
        if comment.upvoted_by.filter(id=request.user.id).exists():
            return HttpResponseForbidden("You have already upvoted this comment.")
        
        if comment.downvoted_by.filter(id=request.user.id).exists():
            comment.downvoted_by.remove(request.user)
            comment.rating += 1
        
        comment.rating += 1
        comment.upvoted_by.add(request.user)
        comment.save()
        
        post = comment.post
        comments = Comment.objects.filter(post=post)
        return render(request, 'comments.html', {'post': post, 'comments': comments})

@login_required
def downvote_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(Comment_id=comment_id)
        
        # Check if the user has already downvoted the comment
        if comment.downvoted_by.filter(id=request.user.id).exists():
            return HttpResponseForbidden("You have already downvoted this comment.")
        
        if comment.upvoted_by.filter(id=request.user.id).exists():
            comment.upvoted_by.remove(request.user)
            comment.rating -= 1
        
        comment.rating -= 1
        comment.downvoted_by.add(request.user)
        comment.save()
        
        post = comment.post
        comments = Comment.objects.filter(post=post)
        return render(request, 'comments.html', {'post': post, 'comments': comments})
    
#-----------------Profile-----------------#

    


from django.shortcuts import render,redirect
from .models import Post,Profile
from django.contrib.auth.decorators import login_required

def feed(request):
    posts= Post.objects.all().order_by('-created_at')
    return render(request,'feed.html',{'posts':posts})

def like_post(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('feed')

def follow_user(request,user_id):
    profile= Profile.objects.get(user_id=user_id)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
    else:
        profile.followers.add(request.user)
    return redirect('feed')





# Create your views here.

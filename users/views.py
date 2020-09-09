from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User


@login_required
def follow_toggle(request, id):
    user = request.user

    followed_user = get_object_or_404(User, pk=id)

    is_follower = user.profile in followed_user.profile.followers.all()


    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)

    return redirect('home')

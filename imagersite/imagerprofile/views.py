from django.shortcuts import render
from django.contrib.auth.models import User


def all_profiles_page(request):
    users = User.objects.filter(is_active=True).all()
    return render(request, 'profilelist.html', context={'users': users})


def profile_page(request, user_id=1):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return render(request, '404.html')
    return render(request, 'profilepage.html', context={'user': user})

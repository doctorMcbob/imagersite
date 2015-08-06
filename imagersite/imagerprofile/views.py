from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfileForm


def all_profiles_page(request):
    users = User.objects.filter(is_active=True).all()
    return render(request, 'profilelist.html', context={'users': users})


def profile_page(request, user_id=1):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return render(request, 'error.html',
                      context={'error_type': '404 Not Found'})
    return render(request, 'profilepage.html', context={'user': user})


def edit_page(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    user = request.user
    form = ProfileForm(request.POST, instance=user.profile)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/profile/{}'.format(user.id))

    return render(request, 'profile_edit.html', context={"form": form})

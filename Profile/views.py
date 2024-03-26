from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from Profile.forms import RegisterForm, ProfileForm

# class ShowProfilePageView(DetailView):
#     model = Profile
#     template_name = 'profile.html'
#     context_object_name = 'profile'

#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#         context['page_user'] = page_user
#         return context

def profile(request, username):
    user = User.objects.get(username=username)
    profile = user.profile
    return render(
        request,
        "profile.html",
        {
            'profile':profile,
            'username': user.username,
            'image': profile.image.url,
        }
    )


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/login/')
    else:
        form = RegisterForm()
    return render(
        request,
        'registration/signup.html',
        {
            'form': form,
        },
    )
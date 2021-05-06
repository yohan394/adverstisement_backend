from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import SignUpForm, ProfileForm
from .models import Profile
from client.models import Settings
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, CreateView
from django.contrib import messages


def help_save_to_session(request, session_key, value):
    if value is not None:
        request.session[session_key] = value


def help_save_profile_pic(request):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.profile_pic:
        request.session["profile_pic"] = profile.profile_pic.url


def index(request):
    """Placeholder index view"""
    return render(request, 'index/index.html')


def sign_out(request):
    logout(request)
    return redirect('index')



def user_index(request):
    profile = get_object_or_404(Profile, user=request.user)
    """Placeholder index view"""
    request.target = "custom"
    client_id =  User.objects.filter(username = request.user)[0].id
    settings = Settings.objects.filter(info_id = client_id)
    context = {
        'settings_list': settings
    }
    return render(request, 'index/index.html', context)


def sign_in(request):
    def try_getting_user_from_email():
        email = request.POST['username']
        param_password = request.POST['password']
        from_email_user = User.objects.filter(email=email).first()

        if from_email_user is not None:
            real_username = getattr(from_email_user, 'username')
            return authenticate(username=real_username, password=param_password)

        return None

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is None:
            user = try_getting_user_from_email()

        if user is not None:
            login(request, user)
            profile = get_object_or_404(Profile, user=request.user)
            help_save_to_session(request, 'profile_pic', profile.profile_pic.url if profile.profile_pic else None)
            help_save_to_session(request, 'fullname', f'{request.user.first_name} {request.user.last_name}')

            return redirect('index')
        else:
            messages.warning(request, 'your username and password does not match.')
            return redirect('index')
    else:
        messages.error(request, 'internal server error from sign-in. Contact dev for inquiry.')
        return redirect('index')


class SignUp(CreateView):
    model = User
    context_object_name = 'user'
    template_name = 'index/forms/signup/form.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        super(SignUp, self).form_valid(form)

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)

        request = self.request
        login(request, user)

        profile = get_object_or_404(Profile, user=request.user)
        help_save_to_session(request, 'profile_pic', profile.profile_pic.url if profile.profile_pic else None)
        help_save_to_session(request, 'fullname', f'{request.user.first_name} {request.user.last_name}')

        return HttpResponseRedirect(self.get_success_url())


class UpdateProfile(UpdateView):
    model = Profile
    context_object_name = 'profile'
    form_class = ProfileForm
    template_name = 'index/forms/profile/form.html'
    success_url = '/'

    def get_object(self):
        profile = get_object_or_404(Profile, user=self.request.user)
        return profile

    def form_valid(self, form):
        form.save()

        request = self.request
        profile = get_object_or_404(Profile, user=request.user)
        help_save_to_session(request, 'profile_pic', profile.profile_pic.url if profile.profile_pic else None)
        help_save_to_session(request, 'fullname', f'{request.user.first_name} {request.user.last_name}')

        return super(UpdateProfile, self).form_valid(form)

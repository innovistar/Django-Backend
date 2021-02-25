from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required
from users.models import Account
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.conf import settings
from django.core.mail import send_mail

#from courses.models import Course

from users.forms import SignUpForm, AccountAuthenticationForm
from users.tokens import account_activation_token


@login_required
def home(request):
    if request.user.is_authenticated:
        #courses = Course.objects.filter(user = request.user)
        #context = {'courses':courses}
        return render(request, 'users/account.html', {'context':context})
    else:
        return redirect('/')

def signup(request):
    context = {}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            #user.is_staff = False
            #user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('users/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_to = user.email
            print(send_to)
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, [send_to], fail_silently=False)
            #login(request, user)
            return redirect('account_activation_sent')
        else:
            context['registration_form'] = form

    else:
        form = SignUpForm()
        context['registration_form'] = form
    return render(request, 'users/signup.html', context)


def login_view(request):
    context = {}
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
    else:
        form = AccountAuthenticationForm()
        context['login_form'] = form
    return render(request, "users/login.html", context)


def account_activation_sent(request):
    return render(request, 'users/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_staff = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'users/account_activation_invalid.html')
    return render(request, 'users/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'users/account_activation_sent.html')


def authenticate(request):
    return render(request, 'users/auth.html', {})


#from django.shortcuts import render
#, redirect
#from django.views import View
#from django.http import JsonResponse
#from django.contrib.auth.models import User

#import json


#class UsenameValidationView(View):
#    def post(self, request):
#        data = json.loads(requst.body)
#        username = data['username']

#        if User.objects.filter(username=username).exists():
#            return JsonResponse({'username_error': 'username already exists'}, status=400)
#        
#        return JsonResponse({'username_valid': True})
        
        

#class RegistrationView(View):
#    def get(self, request):
#        return render(request, 'users/register.html')


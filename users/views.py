from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from .token import account_activation_token
from django.contrib.auth import login, logout, authenticate
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
# Create your views here.


def activate_email(request, user, to_email):
    mail_sub = "LUXE | Activate your user account"
    message = render_to_string("activate_account.html", {
        "user": user,
        "domain": get_current_site(request).domain,
        "uid": urlsafe_base64_encode(force_bytes(user.id)),
        "token": account_activation_token.make_token(user),
        "protocol": "https" if request.is_secure() else "http"
    })
    email = EmailMessage(mail_sub, message, to=[to_email])
    # lA DECLARACION DE ABAJO SIRVE PARA QUE EL CORREO NO LLEGUE COMO TEXTO PLANO Y SE LE PUEDA DAR STYLOS
    email.content_subtype = "html"
    if email.send():
        messages.success(request, "Check your email to verifications")
    else:
        messages.error(
            request, f"Problem sending confirmation email {to_email}, check if your type is correctly")


def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activate")
    else:
        messages.error(request, "Activate link is invalid")

    return redirect("signin")


@user_not_authenticated
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('home')
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {
        'form': form
    })


def redirect_signin_with_google(request):
    messages.error(
        request, "Something wrong here, it may be that you already have account!")
    return redirect("signin")


def redirect_signin_whith_google_cancel(request):
    return redirect('signin')


def redirect_signin_with_google_3rdparty(request):
    messages.error(
        request, "Something wrong here, it may be that you already have account!")
    return redirect("signin")


def redirect_signin_with_google_cancel_3rdparty(request):
    return redirect('signin')


@user_not_authenticated
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,  f"Welcome {request.user.first_name} {
                                 request.user.last_name}")
                return redirect('home')
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {
        'form': form
    })


@login_required(login_url='signin')
def closesession(request):
    logout(request)
    messages.info(request, 'The session was closed')
    return redirect('home')

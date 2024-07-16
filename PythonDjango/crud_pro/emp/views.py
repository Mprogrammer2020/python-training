from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from .models import CustomUser  
from .forms import CustomUserCreationForm, UserLoginForm, CustomUserChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Send welcome email
            subject = 'SEND MAIL'
            message = 'Welcome to join us!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]  # Assuming CustomUser model has an email field
            send_mail(subject, message, email_from, recipient_list)

            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_list')
            else:
                error = "Invalid email pr password. Please try again."
                return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_list(request):
    queryset = CustomUser.objects.all()

    # Search functionality
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(Q(username__icontains=query) | Q(email__icontains=query))

    # Pagination
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Check if queryset is empty
    if query and not page_obj.object_list.exists():
        message = "No such user found."
    else:
        message = None

    return render(request, 'profile_list.html', {'page_obj': page_obj, 'query': query, 'message': message})

@login_required
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile_list')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

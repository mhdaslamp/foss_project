# busportal/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            adm_no = form.cleaned_data['adm_no']
            password = form.cleaned_data['password']
            user = authenticate(request, adm_no=adm_no, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_details')  # Redirect to user details page
            else:
                messages.error(request, 'Invalid admission number or password.')
    else:
        form = LoginForm()
    return render(request, 'sign.html', {'form': form})
    


login_required
def user_details_view(request):
    user = request.user
    try:
        user_details = CustomUser.objects.get(adm_no=user.adm_no)  # Fetch user details using adm_no
        context = {
            'adm_no': user_details.adm_no,
            'name': user_details.name,
            'place': user_details.place,
            'amount': user_details.amount,
        }
        return render(request, 'user_details.html', context)
    except CustomUser.DoesNotExist:
        # Handle case where user does not exist
        return render(request, 'user_details.html', {'error_message': 'User details not found.'})
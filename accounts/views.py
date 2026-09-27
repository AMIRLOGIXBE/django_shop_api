from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from accounts.forms import Sign_Up, Login_form

User = get_user_model()


def signup(request):
    if request.method == "POST":
        form = Sign_Up(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                username=username,
                password=password,
                phone=phone,
            )
            login(request, user)
            return redirect('/shop')  # بعد از ثبت‌نام برو به صفحه اصلی
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = Sign_Up()
        return render(request, 'signup.html', {'form': form})
def Login_view(request):
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = Login_form()
        return render(request, 'login.html', {'form': form})
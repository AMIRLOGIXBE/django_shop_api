from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class Sign_Up(forms.Form):
    username = forms.CharField(max_length=100, label="نام کاربری")
    phone = forms.CharField(max_length=11, label="شماره تماس")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label="رمز عبور")
    two_password = forms.CharField(max_length=100, widget=forms.PasswordInput, label="تکرار رمز عبور")

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise ValidationError('نام کاربری را وارد کنید')
        if username == 'hack':
            raise ValidationError('این نام کاربری قابل ثبت نیست')
        if User.objects.filter(username=username).exists():
            raise ValidationError('این نام کاربری قبلاً گرفته شده')
        return username

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise ValidationError('شماره تماس فقط باید عدد باشد')
        if len(phone) != 11:
            raise ValidationError('شماره تماس باید ۱۱ رقم باشد')
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('two_password')

        if password and password2 and password != password2:
            raise ValidationError('رمز عبور و تکرار آن یکسان نیستند')

        return cleaned_data


from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class Login_form(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام کاربری خود را وارد کنید'
        })
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'پسورد خود را وارد کنید'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # اگه هر دو پر بودن، authenticate کن
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("نام کاربری یا رمز عبور اشتباه می باشد")
            self.user_cache = user

        return cleaned_data

    def get_user(self):
        return getattr(self, 'user_cache', None)




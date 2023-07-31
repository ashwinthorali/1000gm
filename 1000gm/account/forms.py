from django import forms                
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit =True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user    
    def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder':'Username without spaces', 'onkeyup':'userCheck()'}
            self.fields['email'].widget.attrs = {'class': ' form-control' }
            self.fields['password1'].widget.attrs = {'class': ' form-control' }
            self.fields['password2'].widget.attrs = {'class': ' form-control', 'onkeyup': 'pwfun()' }
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name"]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control'}

class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder':'Full Name'}
        
        
    class Meta:
        model = Profile
        fields = '__all__'
            

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }                
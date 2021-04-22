from django import forms

from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(required=True,)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class AvatarForm(forms.ModelForm):
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.profile.image = self.cleaned_data['avatar']
        user.profile.save()
        return user
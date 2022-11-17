from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from .models import Room, User


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['name','username','email']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['name','username','email']


class RoomForm(ModelForm):
    
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']

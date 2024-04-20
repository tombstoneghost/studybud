from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Room


# Create Form Class
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


# Update User Form
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

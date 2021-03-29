from .models import Group, User
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'group']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']


from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .forms import GroupForm, UserForm
from .models import Group, User
from django.contrib import messages


def users(request):
    # Method that render all User object's(main page)
    all_users = User.objects.all()
    return render(request, 'main/users.html', {'all_users': all_users})


def groups(request):
    # Method that render all Group object's(groups page)
    all_groups = Group.objects.all()
    return render(request, 'main/groups.html', {'all_groups': all_groups})


def create_user(request):
    # Method that create User object
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            error = 'Something not right'
    form = UserForm()
    all_users = User.objects.all()

    data = {
        'all_users': all_users,
        'form': form,
        'error': error
    }

    return render(request, 'main/create_user.html', data)


def create_group(request):
    # Method that create Group object
    error = ''
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
        else:
            error = 'Something not right'

    form = GroupForm()
    all_groups = Group.objects.all()

    data = {
        'all_groups': all_groups,
        'form': form,
        'error': error
    }

    return render(request, 'main/create_group.html', data)


class UserEditor(UpdateView):
    # Class that update User object's
    model = User
    template_name = 'main/edit_user.html'
    fields = ['nickname', 'group']
    context_object_name = 'user'


class GroupEditor(UpdateView):
    # Class that update Group object's
    model = Group
    template_name = 'main/edit_group.html'
    fields = ['name', 'description']
    context_object_name = 'group'


def delete_user(request, pk):
    # Method that delete User object's
    user = User.objects.get(id=pk)
    user.delete()
    return HttpResponseRedirect("/")


def delete_group(request, pk):
    # Method that delete Group object's
    try:
        group = Group.objects.get(id=pk)
        group.delete()
        messages.info(request, 'Group deleted!')
        return HttpResponseRedirect("/groups")
    except:
        messages.info(request, "You can't delete the group with existing users in it!")
        return HttpResponseRedirect("/groups")

from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name="users"),
    path('groups', views.groups, name="groups"),
    path('create_user', views.create_user, name='create_user'),
    path('create_group', views.create_group, name='create_group'),
    path('edit_user/<int:pk>', views.UserEditor.as_view(), name='edit_user'),
    path('edit_group/<int:pk>', views.GroupEditor.as_view(), name='edit_group'),
    path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
    path('delete_group/<int:pk>', views.delete_group, name='delete_group'),
]


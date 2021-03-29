from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=50, db_index=True, verbose_name='Name')
    group = models.ForeignKey('Group', null=True, on_delete=models.PROTECT, verbose_name='Group')
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date')

    def get_absolute_url(self):
        return '/'


class Group(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Name')
    description = models.TextField(max_length=255, verbose_name='Description')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/groups'


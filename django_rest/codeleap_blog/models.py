from django.db import models
from django.utils.timezone import now as django_now



class Blogpost(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=50, verbose_name='Username')
    created_datetime = models.DateTimeField(default=django_now, editable=False)
    title = models.CharField(max_length=140)
    content = models.TextField(max_length=2097152, verbose_name='') # Allowing roughly 2MB of ASCII text

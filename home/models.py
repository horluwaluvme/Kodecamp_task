
from sqlite3 import Timestamp  
from django.db import models

# Create your models here.
class Post(models.Model):
    post_name = models.CharField(max_length=500)
    post_content = models.CharField(max_length=500)
    Timestamp = models.DateTimeField(auto_now_add=True)


#python manage.py makemigration
#python manage.py migrate


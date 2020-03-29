from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    author_name = models.CharField(max_length = 100)
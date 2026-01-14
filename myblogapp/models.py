from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length= 50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length= 50)

    def __str__(self):
        return self.username
    
class blog_list(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

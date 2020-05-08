from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user            = models.ForeignKey(User, on_delete= models.CASCADE)
    firstname       = models.CharField(max_length = 200)
    lastname        = models.CharField(max_length = 200)
    email           = models.EmailField(max_length= 254)
    phone           = models.CharField(max_length = 200)
    username        = models.CharField(max_length = 50)
    password        = models.CharField(max_length = 18)
    date_registered = models.DateTimeField(auto_now_add=True)
    is_active       = models.BooleanField(default=True)
    
    
    
    def __str__(self):
        return self.username
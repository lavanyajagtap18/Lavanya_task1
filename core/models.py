from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    followers=models.ManyToManyField(
        User,related_name="following",blank=True
    )

    def __str__(self):
        return self.user.username
    
class Post(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
    
class Comment(models.Model):
    Post= models.ForeignKey(Post,on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    text= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)



    
    
        

      

# Create your models here.
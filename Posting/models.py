from django.db import models
from UserAuth.models import User
# Create your models here.
class Post(models.Model):
    Post_Name=models.CharField(max_length=50,verbose_name="Post_Title",unique=True)
    Description=models.TextField()
    Draft=models.BooleanField(default=False)
    Image=models.ImageField(upload_to='posts_images',default='default.jpg',null=True,blank=True)
    # Author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Author')

    def __str__(self):
        return str(self.Post_Name)
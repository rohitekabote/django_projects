from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    des = RichTextUploadingField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination_name = models.ForeignKey(Destination, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, default=None)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)  # Many-to-Many for likes
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)

    def total_likes(self):
        return self.likes.count()  # Count total likes
    
    def total_dislikes(self):
        return self.dislikes.count()  # Count total dislikes

    def __str__(self):
        return self.comment
    
   
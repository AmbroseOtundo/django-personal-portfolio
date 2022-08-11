from django.db import models

class Projectblog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=550)
    image = models.ImageField(upload_to='blog/images')
    date = models.DateTimeField()
    url = models.URLField(blank=True)
   

        
# able to see the name  of the specific object in the admin instead of object

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class team(models.Model):
    nme=models.CharField(max_length=250)
    propic=models.ImageField(upload_to='img')
    about=models.TextField()

    def __str__(self):
        return self.nme

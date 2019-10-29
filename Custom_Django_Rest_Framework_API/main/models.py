from django.db import models

# Create your models here.
class File(models.Model):

    #what we want in our model
    file = models.FileField(blank=False, null=False)   #place to hold the file
    remark = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField



class Blogs(models.Model):
    title = models.CharField(max_length=200)
    short = models.CharField(max_length=2000,null=True)
    description =  RichTextField(blank=True , null=True) 
    created_at = models.CharField(max_length=100)
    img = models.CharField(max_length=100 , null=True)


    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    cardImage = models.CharField(max_length=200)

    model_taget = models.CharField(max_length=200,unique=True)
    model_imgage = models.CharField(max_length=200)
    models_description = RichTextField(blank=True , null=True)



    def __str__(self):
        return self.title
    
from django.db import models

# Modelos de Usuario para el inicio de sesion:



class CompanyMember(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='members_images')
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
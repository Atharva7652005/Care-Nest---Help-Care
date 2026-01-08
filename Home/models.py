from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Add_Orphanage(models.Model):
    orpho_name = models.CharField(max_length=100)
    orpho_type = models.CharField(max_length=50)
    orpho_city = models.CharField(max_length=100)
    orpho_email = models.EmailField()
    orpho_caretaker_name = models.CharField(max_length=100)
    orpho_no_residentials = models.IntegerField()
    orpho_contact_no = models.CharField(max_length=11)
    orpho_address = models.TextField()
    orpho_description = models.TextField()
    orpho_requirements = models.TextField()
    orpho_image = models.ImageField(upload_to="orpho_images")

class Orphanage_Feedback(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    sender_message = models.CharField(max_length=500)
    sender_rating = models.IntegerField()
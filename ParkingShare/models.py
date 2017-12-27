from django.db import models

class User(models.Model):
    phoneNumber = models.TextField()
    password = models.TextField()
    name = models.TextField()
    surname = models.TextField()
    city = models.TextField()
    sex = models.TextField()
    date_of_birth = models.TextField()

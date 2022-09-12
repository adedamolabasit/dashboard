from django.db import models

# Create your models here.


class Enquiry(models.Model):
    name=models.CharField(max_length=51)
    email=models.EmailField()
    timeline=models.TextField()
    information=models.TextField()

    def __str__(self):
        return f"{self.name}|{self.email}"

class NewsLetter(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email

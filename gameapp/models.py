from django.db import models

# Create your models here.

class Gameapp(models.Model):
    random_word = models.CharField(max_length=250)
    display_word = models.CharField(max_length=250)
    alphabet_key = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=250, null=True)
    guessed = models.CharField(max_length=30, default="")
    wrong = models.CharField(max_length=30, default="")
    alphabets = models.CharField(max_length=30, default="")
    #picture = models.ImageField(upload_to="gallery")
    #no_of_tries = models.IntegerField(default=7)

    def __str__(self):
        return self

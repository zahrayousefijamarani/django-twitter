from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=200)
    photo_string = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    background = models.CharField(max_length=400, default="../../static/awesomeTwitter/profile/mountain-1.jpg")
    password = models.CharField(max_length=200,default=12)

    class Meta:
        permissions = (
            ('see_main_page', 'go_others_page'),
        )


class Message(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

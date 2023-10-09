from django.db import models

# Create your models here.


class Monster(models.Model):
    name = models.CharField(max_length=120)
    ac = models.IntegerField()
    hp = models.IntegerField()
    level = models.IntegerField()
    attacks = models.CharField(max_length=200)
    movement = models.CharField(max_length=200)
    morale = models.CharField(max_length=100)
    number_appearing = models.CharField(max_length=100)
    extra_info = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"{self.name}."

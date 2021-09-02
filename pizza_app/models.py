from django.db import models


class Piz_Mod(models.Model):
    PIZZA_CHOICES = (
        ("Regular", "Regular"),
        ("Square", "Square"),
    )
    pid = models.SlugField(max_length=200)
    type = models.CharField(max_length=50,choices=PIZZA_CHOICES)
    size= models.CharField(max_length=50)
    toppings = models.CharField(max_length=50)

    def __str__(self):
        return self.type
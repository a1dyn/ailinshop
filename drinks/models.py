from django.db import models

class Drink(models.Model):
    drinks = [
        ('Cola', "Coca Cola"),
        ('Fanta', "Fanta"),
        ('Sprite', "Sprite"),
        ('Fuse', "Fuse tea"),
        ('Maxi', "Maxi tea"),    
        ('Piko', "Piko"),
    ]
    drink_name = models.CharField(max_length=10, choices=drinks, default="Coca Cola")
    amount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default= 0)

    def __str__(self) -> str:
        return f"{self.drink_name},{self.amount}, {self.price}"
    
    def save(self, *args, **kwargs):
        exists = Drink.objects.filter(drink_name=self.drink_name).first()
        if exists:
            exists.amount += self.amount
            if exists.price < self.price:
                exists.price = self.price
            super(Drink, exists).save(*args, **kwargs)
        else:
            super(Drink, self).save(*args, **kwargs)


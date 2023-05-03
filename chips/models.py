from django.db import models

class Chips(models.Model):
    chips = [
        ('Lays', "Lays"),
        ('Slang', "Slang"),
        ('Grizly', "Grizly"),
        ('Fan', "Fan"),
        ('Flint', "Flint"),
        ('Grenki', "Grenki"),
    ]
    chips_name = models.CharField(max_length=10, choices=chips, default="Lays")
    amount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default= 0)

    def __str__(self) -> str:
        return f"{self.chips_name},{self.amount}, {self.price}"
    
    def save(self, *args, **kwargs):
        exists = Chips.objects.filter(chips_name=self.chips_name).first()
        if exists:
            exists.amount += self.amount
            if exists.price < self.price:
                exists.price = self.price
            super(Chips, exists).save(*args, **kwargs)
        else:
            super(Chips, self).save(*args, **kwargs)


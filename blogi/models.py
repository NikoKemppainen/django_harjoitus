from django.db import models


class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField()
    kuva = models.ImageField(null=true)
    luotu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.otsikko
    
    def luo_ingressi(self):
        if self.ingressi:
            return self.ingressi
        return self.tekstit[:50] + "..."
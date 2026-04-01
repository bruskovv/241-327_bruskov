from django.db import models

class Perfume(models.Model):
    name = models.CharField(max_length=150)  # имя
    brand = models.CharField(max_length=100)  # бренд
    volume_ml = models.IntegerField()  # обьем
    price = models.DecimalField(max_digits=8, decimal_places=2)  # цена
    alcohol_percent = models.FloatField()  # содержание спирта(в %)
    is_in_stock = models.BooleanField(default=True)  # наличие
    release_year = models.DateField()  # год выпуска
    notes = models.TextField(blank=True)  # ноты аромата(верхние/средние/нижние)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.volume_ml}ml)"

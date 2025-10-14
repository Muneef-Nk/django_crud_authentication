from django.db import models
from django.utils import timezone

class Crud(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    quantity = models.PositiveIntegerField()
    rating = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # max 10 after . only 2
    is_active = models.BooleanField(default=False)

    # date = models.DateField(default= timezone.now)
    # time = models.TimeField(default=timezone.now)
    # created_at = models.DateTimeField()  # Fixed

    email = models.EmailField()
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.name


# Rule of thumb:

# null → database

# blank → validation (forms/serializers)
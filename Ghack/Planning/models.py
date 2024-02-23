
from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    next = models.DateField()

    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.source

class Debt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    minimum_payment = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return self.name

class Goal(models.Model):
    user = models.ForeignKey(User, related_name='goals', on_delete=models.CASCADE)
    goal = models.TextField()
    date_set = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Goal for {self.user.username}"
    



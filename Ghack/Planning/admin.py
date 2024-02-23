from django.contrib import admin
from .models import Expense, Income, Debt , Goal

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Debt)
admin.site.register(Goal)
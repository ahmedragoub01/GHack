from django.contrib import admin
from .models import BudgetCategory, Expense, Income, Debt

admin.site.register(BudgetCategory)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Debt)
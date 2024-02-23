from datetime import timedelta
from django.shortcuts import render
from requests import Response
from .models import  Expense, Income, Debt, Goal
from django.http import JsonResponse , HttpResponse
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request, 'Planning/index.html')

#-----------------------------------Goals--------------------------------------#

@login_required
def get_goal(request , user_id):
    goals = Goal.objects.filter(user=user_id)
    goals = goals.order_by('-date_set')
    goal = goals[0]
    return render(request, 'Planning/goal.html', {'goal': goal})

@login_required
def add_goal(request , user_id):
    if request.method == 'POST':
        goal = Goal()
        goal.user = user_id
        goal.title = request.POST['title']
        goal.description = request.POST['description']
        goal.date_set = request.POST['date_set']
        goal.date_due = request.POST['date_due']
        goal.save()
        pass
    else:
        render(request, 'Planning/add_goal.html')

@login_required
def delete_goal(request , user_id, goal_id):
    goal = Goal.objects.get(id=goal_id)
    goal.delete()
    pass

@login_required
def edit_goal(request , user_id, goal_id):
    if request.method == 'POST':
        goal = Goal.objects.get(id=goal_id)
        goal.title = request.POST['title']
        goal.description = request.POST['description']
        goal.date_set = request.POST['date_set']
        goal.date_due = request.POST['date_due']
        goal.save()
        pass
    else:
        render(request, 'Planning/edit_goal.html')

#-----------------------------------Budget--------------------------------------#

# Add the login_required decorator to the budget-related views as well

#---------------------------------expenses--------------------------------------#

@login_required
def get_expenses(request):

    
    user = request.user
    expenses = Expense.objects.filter(user=user)
    
    context = {
        'expenses': expenses
    }

    return render(request, 'Planning/index.html', context)

@login_required
def add_expense(request):
    user = request.user
    if request.method == 'POST':
        expense = Expense()
        expense.user = user
        expense.name = request.POST['name']
        expense.amount = request.POST['amount']
        expense.date = request.POST['date']
        expense.type = request.POST['type']
        expense.category = request.POST['category']
        expense.save()
        return HttpResponse('Expense added successfully')
    else:
        render(request, 'Planning/add_expense.html')

@login_required
def delete_expense(request):
    user = request.user
    expense = Expense.objects.get(user=user)
    expense.delete()
    pass

@login_required
def edit_expense(request , expense_id):
    if request.method == 'POST':
        expense = Expense.objects.get(id=expense_id)
        expense.name = request.POST['name']
        expense.amount = request.POST['amount']
        expense.date = request.POST['date']
        expense.type = request.POST['type']
        expense.category = request.POST['category']
        expense.save()
        pass
    else:
        render(request, 'Planning/edit_expense.html')

#---------------------------------income--------------------------------------#

@login_required
def get_income(request,user):
    income = Income.objects.filter(user=user)
    return income

@login_required
def get_total_income(request):
    user = request.user
    income = get_income(user)
    total = 0
    for i in income:
        total += i.amount
    return total

#---------------------------------debt--------------------------------------#

@login_required
def get_debt(request , user_id):
    debt = Debt.objects.filter(user=user_id)
    return debt

@login_required
def get_total_debt(request , user_id):
    debt = get_debt(user_id)
    total = 0
    for d in debt:
        total += d.balance
    return total

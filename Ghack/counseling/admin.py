from django.contrib import admin
from .models import Post, Comment , FinancialCounselor, Consultation, Message 


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FinancialCounselor)
admin.site.register(Consultation)
admin.site.register(Message)

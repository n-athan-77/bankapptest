from django.contrib import admin
from .models import *


admin.site.register(Branch)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(BankUser)
admin.site.register(Card)
admin.site.register(Atm)


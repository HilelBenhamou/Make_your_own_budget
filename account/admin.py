from django.contrib import admin

# Register your models here.

from account.models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'balance_start', 'balance', 'user']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['amount', 'object', 'comment', 'account', 'status', 'transaction_date']


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

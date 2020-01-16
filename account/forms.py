from django.forms import Form, ModelForm
from django.contrib.auth.forms import UserCreationForm
from account.models import Account, Transaction


class CreateAccountForm(Form, ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'balance_start', 'currency']


class TransactionForm(Form, ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'object', 'comment', 'status']
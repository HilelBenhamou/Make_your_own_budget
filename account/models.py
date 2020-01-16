from django.db import models
from django.contrib.auth.forms import User
from datetime import datetime
# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=30)
    balance = models.FloatField(default=0)
    currency = models.CharField(max_length=30, choices=[('₪', '₪'), ('$', '$'), ('€', '€')])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    balance_start = models.FloatField(default=0)
    date_creation = models.DateField(null=True)


class Transaction(models.Model):
    amount = models.FloatField()
    object = models.CharField(max_length=30, choices=[('Food', 'Food'), ('Education', 'Education'), ('Shopping','Shopping'), ('Personal Care', 'Personal Care'), ('Health & Fitness', 'Health & Fitness'), ('Kids', 'Kids'), ('Food & Dining', 'Food & Dining'), ('Gifts & Donations', 'Gifts & Donations'),('Auto & Transport','Auto & Transport'),('Travel','Travel'),('Fees & Charges','Fees & Charges'),('Taxes', 'Taxes'), ('Investments', 'Investments')])
    comment = models.CharField(max_length=200)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=30, choices=[('Debit','Debit'), ('Credit','Credit')])
    transaction_date = models.DateTimeField()

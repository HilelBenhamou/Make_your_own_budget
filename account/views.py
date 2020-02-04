from django.shortcuts import render, redirect
from account.forms import CreateAccountForm, TransactionForm
from account.models import Account, Transaction
from django.contrib.auth.forms import User
from django.db.models import Sum

from datetime import datetime


# Create your views here.


def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)

        if form.is_valid():
            new_account = Account(
                name=form.cleaned_data['name'],
                user=request.user,
                balance_start=form.cleaned_data['balance_start'],
                balance=form.cleaned_data['balance_start'],
                currency=form.cleaned_data['currency'],
                date_creation=datetime.now().strftime('%Y-%m-%d'),
            )
            new_account.save()
            return redirect('my_profile')
    else:
        form = CreateAccountForm()
        return render(request, 'account/create_account.html', {'form': form})


def transaction(request, account_id):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        account = Account.objects.get(id=account_id)
        if form.is_valid():
            new_transaction = Transaction(
                amount=form.cleaned_data['amount'],
                object=form.cleaned_data['object'],
                comment=form.cleaned_data['comment'],
                account=account,
                status=form.cleaned_data['status'],
                transaction_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
            new_transaction.save()
            if new_transaction.status == 'Debit':
                update_account = Account.objects.get(id=new_transaction.account.id)
                update_account.balance = update_account.balance - new_transaction.amount
                update_account.save()
            elif new_transaction.status == 'Credit':
                update_account = Account.objects.get(id=new_transaction.account.id)
                update_account.balance = update_account.balance + new_transaction.amount
                update_account.save()
            return redirect('book_account')

    else:
        form = TransactionForm()
        accounts = Account.objects.filter(user=request.user)
        current_account = Account.objects.get(id=account_id)
        today_date = datetime.now().strftime('%b. %d, %Y')
        return render(request, 'account/transaction.html',
                      {'form': form, 'accounts': accounts, 'current_account': current_account,
                       'today_date': today_date})


def book_account(request, account_id):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        account = Account.objects.get(id=account_id)
        if form.is_valid():
            new_transaction = Transaction(
                amount=form.cleaned_data['amount'],
                object=form.cleaned_data['object'],
                comment=form.cleaned_data['comment'],
                account=account,
                status=form.cleaned_data['status'],
                transaction_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
            new_transaction.save()
            if new_transaction.status == 'Debit':
                update_account = Account.objects.get(id=new_transaction.account.id)
                update_account.balance = update_account.balance - new_transaction.amount
                update_account.save()
            elif new_transaction.status == 'Credit':
                update_account = Account.objects.get(id=new_transaction.account.id)
                update_account.balance = update_account.balance + new_transaction.amount
                update_account.save()
            current_account = Account.objects.get(id=account_id)
            transactions = Transaction.objects.all()
            today_date = datetime.now().strftime('%b. %d, %Y')

            return render(request, 'account/book_account.html',
                          {'form': form, 'transactions': transactions, 'current_account': current_account,
                           'today_date': today_date})

    else:
        form = TransactionForm()
        current_account = Account.objects.get(id=account_id)
        transactions = Transaction.objects.all()
        today_date = datetime.now().strftime('%b. %d, %Y')

        return render(request, 'account/book_account.html',
                      {'form': form, 'transactions': transactions, 'current_account': current_account,
                       'today_date': today_date})


def account(request):
    all_accounts = Account.objects.filter(user=request.user)
    return render(request, 'account/account.html', {'all_accounts': all_accounts})


def delete_account(request, account_id):
    account = Account.objects.get(id=account_id)
    account.delete()
    return redirect('my_profile')


def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    current_account = Account.objects.get(id=transaction.account.id)
    transaction.delete()
    transactions = Transaction.objects.all()
    today_date = datetime.now().strftime('%b. %d, %Y')

    if transaction.status == 'Debit':
        update_account = Account.objects.get(id=transaction.account.id)
        update_account.balance = update_account.balance + transaction.amount
        update_account.save()
    elif transaction.status == 'Credit':
        update_account = Account.objects.get(id=transaction.account.id)
        update_account.balance = update_account.balance - transaction.amount
        update_account.save()
    return redirect('book_account', account_id=current_account.id)
    # return render(request, 'account/book_account.html',
    #               {'transactions': transactions, 'current_account': current_account,
    #                'today_date': today_date})


def my_stat(request, account_id):
    account = Account.objects.get(id=account_id)
    transaction = Transaction.objects.filter(account=account)
    total_food = 0
    total_education = 0
    total_shopping = 0
    total_perso = 0
    total_kids = 0
    total_transport = 0

    # t_food = Transaction.objects.filter(object='Food', account=account)
    # t_education = Transaction.objects.filter(object='Education', account=account)
    # t_shopping = Transaction.objects.filter(object='Shopping', account=account)
    # t_perso = Transaction.objects.filter(object='Personal Care', account=account)
    # t_kids = Transaction.objects.filter(object='Kids', account=account)
    # t_transport = Transaction.objects.filter(object='Auto & Transport', account=account)
    #
    # context = {}
    # for category, _ in Transaction.objects.choices:
    #     data = Transaction.objects.filter(object=category, account=account)
    #     if data:
    #         total = data.aggregate(Sum('amount'))
    #         context[category] = {'total': total, 'stat': round(total * 100 / account.balance_start, 2)}
    #
    # for info in t_food:
    #     object_food = info.object
    #     total_food += info.amount
    #     stat_food = round(total_food * 100 / account.balance_start, 2)
    #
    # for info in t_education:
    #     object_educ = info.object
    #     total_education += info.amount
    #     stat_educ = round(total_food * 100 / account.balance_start, 2)
    #
    # for info in t_shopping:
    #     object_shop = info.object
    #     total_shopping += info.amount
    #     stat_shop = round(total_food * 100 / account.balance_start, 2)
    #
    # for info in t_perso:
    #     object_perso = info.object
    #     total_perso += info.amount
    #     stat_perso = round(total_food * 100 / account.balance_start, 2)
    #
    # for info in t_kids:
    #     object_kids = info.object
    #     total_kids += info.amount
    #     stat_kids = round(total_food * 100 / account.balance_start, 2)
    #
    # for info in t_transport:
    #     object_transport = info.object
    #     total_transport += info.amount
    #     stat_transport = round(total_food * 100 / account.balance_start, 2)
    #
    # return render(request, 'account/my_stat.html',
    #               {'account': account, 'total_food': total_food, 'object_perso': object_perso,
    #                'total_perso': total_perso, 'stat_perso': stat_perso, 'object_kids': object_kids,
    #                'total_kids': total_kids, 'stat_kids': stat_kids, 'object_transport': object_transport,
    #                'total_transport': total_transport, 'stat_transport': stat_transport,
    #                'total_education': total_education, 'total_shopping': total_shopping,
    #                'stat_food': stat_food,
    #                'stat_educ': stat_educ, 'stat_shop': stat_shop, 'object_food': object_food,
    #                'object_educ': object_educ, 'object_shop': object_shop})

    for one in transaction:
        if one.object == 'Food':
            object_food = one.object
            total_food += one.amount
            stat_food = round(total_food * 100 / account.balance_start, 2)

        elif one.object == 'Education':
            object_educ = one.object
            total_education += one.amount
            stat_educ = round(total_education * 100 / account.balance_start, 2)

        elif one.object == 'Shopping':
            object_shop = one.object
            total_shopping += one.amount
            stat_shop = round(total_shopping * 100 / account.balance_start, 2)

        elif one.object == 'Personal Care':
            object_perso = one.object
            total_perso += one.amount
            stat_perso = round(total_perso * 100 / account.balance_start, 2)

        elif one.object == 'Kids':
            object_kids = one.object
            total_kids += one.amount
            stat_kids = round(total_kids * 100 / account.balance_start, 2)

        elif one.object == 'Auto & Transport':
            object_transport = one.object
            total_transport += one.amount
            stat_transport = round(total_transport * 100 / account.balance_start, 2)

            return render(request, 'account/my_stat.html',
                          {'account': account, 'total_food': total_food, 'object_perso': object_perso,
                           'total_perso': total_perso, 'stat_perso': stat_perso, 'object_kids': object_kids,
                           'total_kids': total_kids, 'stat_kids': stat_kids, 'object_transport': object_transport,
                           'total_transport': total_transport, 'stat_transport': stat_transport,
                           'total_education': total_education, 'total_shopping': total_shopping,
                           'stat_food': stat_food,
                           'stat_educ': stat_educ, 'stat_shop': stat_shop, 'object_food': object_food,
                           'object_educ': object_educ, 'object_shop': object_shop})

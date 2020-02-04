from django.urls import path
from account import views

urlpatterns = [
    path('create_account', views.create_account, name='create_account'),
    path('transaction/<int:account_id>', views.transaction, name='transaction'),
    path('book_account/<int:account_id>', views.book_account, name='book_account'),
    path('delete_account/<int:account_id>', views.delete_account, name='delete_account'),
    path('my_stat/<int:account_id>', views.my_stat, name='my_stat'),
    path('delete_transaction/<int:transaction_id>', views.delete_transaction, name='delete_transaction'),


]
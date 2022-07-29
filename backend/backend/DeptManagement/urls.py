from .views import Register, Login, UserView, Logout, UsersList, Transactions, OwnTransactions, PaidTransaction
from django.urls import path

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('me', UserView.as_view()),
    path('logout', Logout.as_view()),
    path('users', UsersList.as_view()),
    path('transactions', Transactions.as_view()),
    path('transactions/<uuid:id>', Transactions.as_view()),
    path('transactions/<uuid:id>/mark_as_paid', PaidTransaction.as_view()),
    path('own_transaction', OwnTransactions.as_view())
]

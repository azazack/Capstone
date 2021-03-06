from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from ..serializers import TransactionSerializer, GetTransactionSerializer
from rest_framework.response import Response
from ..models import Transaction
from ..modules import authenticated_user
from django.db.models import Q
from ..modules.pagination import CustomPagination

class Transactions(APIView):
    def post(self, request):
        user = authenticated_user(request)
        data = request.data['transaction']
        data['sender'] = user['id']
        serializer = TransactionSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def get(self):
        transactions = Transaction.objects.all()
        serializer = GetTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = self.kwargs['id']
        user = authenticated_user(request)
        transaction = Transaction.objects.filter(pk=id).first()
        transaction_data = request.data['transaction']
        transaction_serializer = TransactionSerializer(transaction, data=transaction_data, partial=True)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
        return JsonResponse(transaction_serializer.errors)


class PaidTransaction(APIView):
    def put(self, request, *args, **kwargs):
        transaction_data = {}
        id = self.kwargs['id']
        transaction = Transaction.objects.filter(pk=id).first()
        transaction_data['paid'] = True
        transaction_serializer = TransactionSerializer(transaction, data=transaction_data, partial=True)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
        return JsonResponse(transaction_serializer.errors)


class OwnTransactions(generics.ListAPIView):
    serializer_class = GetTransactionSerializer

    def get_queryset(self):
        user = authenticated_user(self.request)
        type = self.request.GET.get('type')
        if not type:
            transactions = Transaction.objects.filter(Q(sender=user['id']) | Q(receiver=user['id'])).order_by(
                'paid', '-created_at')
        elif type == 'sent':
            transactions = Transaction.objects.filter(sender=user['id'])
        elif type == 'received':
            transactions = Transaction.objects.filter(receiver=user['id'])
        elif type == 'paid':
            transactions = Transaction.objects.filter(paid=True).filter(Q(sender=user['id']) | Q(receiver=user['id']))
        return transactions

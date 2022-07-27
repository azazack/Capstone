from rest_framework.views import APIView
from ..serializers import TransactionSerializer, GetTransactionSerializer
from rest_framework.response import Response
from ..models import Transaction
from ..modules import authenticated_user
from django.db.models import Q


class Transactions(APIView):
    def post(self, request):
        user = authenticated_user(request)
        data = request.data['transaction']
        data['sender'] = user['id']
        serializer = TransactionSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = GetTransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class OwnTransactions(APIView):
    def get(self, request):
        user = authenticated_user(request)
        type = request.GET.get('type')
        if not type:
            transactions = Transaction.objects.filter(Q(sender=user['id']) | Q(receiver=user['id'])).order_by('-created_at')
        elif type == 'sent':
            transactions = Transaction.objects.filter(sender=user['id'])
        elif type == 'received':
            transactions = Transaction.objects.filter(receiver=user['id'])
        serializer = GetTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

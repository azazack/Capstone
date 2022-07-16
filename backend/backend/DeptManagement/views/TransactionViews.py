from rest_framework.views import APIView
from ..serializers import TransactionSerializer, GetTransactionSerializer
from rest_framework.response import Response
from ..models import Transaction
from ..modules import authenticated_user


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
        transactions = Transaction.objects.filter(sender=user['id'])
        serializer = GetTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

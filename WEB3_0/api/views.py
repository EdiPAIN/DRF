from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import User_Model
from django.http import HttpResponseForbidden
from .serializers import UserSerializer, MoneyTransferSerializer


def user_list_view(request):
    users = User_Model.objects.all()
    return render(request, 'Users_lst.html', {'users': users})


class UserListCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_Model.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        name = request.POST.get('User_Name')
        inn = request.POST.get('User_IIN')
        balance = request.POST.get('All_money')

        if User_Model.objects.filter(User_IIN=inn).exists():
            return render(request, 'add_account.html', {'error': 'Счет с таким ИНН уже существует'})

        account = User_Model(User_Name=name, User_IIN=inn, All_money=balance)
        account.save()

        return redirect('user-list')

    def get(self, request):
        return render(request, 'Create.html')


class TransferViewSet(APIView):
    def post(self, request):
        serializer = MoneyTransferSerializer(data=request.data)
        if serializer.is_valid():
            source_inn = serializer.validated_data.get('source_inn')
            target_inn = serializer.validated_data.get('target_inn')
            amount = serializer.validated_data.get('amount')



            if source_inn == target_inn:
                return Response({"message": "ИИН одинаковые напишите заново."},
                                status=status.HTTP_404_NOT_FOUND)

            try:
                source_account = User_Model.objects.get(User_IIN=source_inn)
                target_account = User_Model.objects.get(User_IIN=target_inn)

                if source_account.All_money >= amount:
                    source_account.All_money -= amount
                    target_account.All_money += amount
                    source_account.save()
                    target_account.save()
                    return Response({"message": "Перевод выполнен успешно."}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Недостаточно средств на счете отправителя."},
                                    status=status.HTTP_400_BAD_REQUEST)

            except User_Model.DoesNotExist:
                return Response({"message": "Один из счетов с указанным ИНН не найден."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        results = User_Model.objects.all
        return render(request, 'index.html', {"User_IIN": results, "All_money": results})

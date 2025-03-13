from rest_framework import viewsets, status
from api.models import *
from api.serializers import *
from django.shortcuts import get_list_or_404
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response    

# class UseerViewSet(viewsets.ModelViewSet):
#     queryset = CustonUser.objects.all()
#     serializer_class = UserSerializer

class User(APIView):
    def get(self, request, id=None):

        if id:
            usuario = get_list_or_404(CustonUser, pk=id)
            serializer = UserSerializer(usuario, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
       
        usuarios = CustonUser.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, pk):
        user = CustonUser.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        user = CustonUser.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        nome = request.data.get('nome')
        senha = request.data.get('senha')

        usuario = authenticate(username=nome, password=senha)

        if (usuario):
            login(request, usuario)
            return Response({'status': status.HTTP_200_OK})
        else:
            return Response({'masage': "Usuário não autenticado", "status": status.HTTP_401_UNAUTHORIZED})
            



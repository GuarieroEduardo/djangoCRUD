from rest_framework import status
from django.contrib.auth.hashers import make_password
from api.models import *
from api.serializers import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response    

# class UseerViewSet(viewsets.ModelViewSet):
#     queryset = CustonUser.objects.all()
#     serializer_class = UserSerializer

class User(APIView):
    def get(self, request, id=None):

        if id:
            usuario = get_object_or_404(CustonUser, pk=id)
            serializer = UserSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
       
        usuarios = CustonUser.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        nome = request.data.get('nome')
        senha = request.data.get('senha')

        if not nome or not senha:
            return Response({'message': 'Os campos "nome" e "senha" são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        usuario = CustonUser.objects.create(
            username=nome,
            password=make_password(senha),
            is_active=True,
            is_aluno=True
        )

        return Response({"message": "Usuário criado com sucesso.", "id": usuario.id}, status=status.HTTP_201_CREATED)


    
    def put(self, request, id):
        usuario = get_object_or_404(CustonUser, pk=id)
        seliazer = UserSerializer(usuario, data=request.data, partial=True)
        if seliazer.is_valid():
            seliazer.save()
            return Response(seliazer.data, status=status.HTTP_200_OK)  
    

    def delete(self, request, pk):
        user = CustonUser.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

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
            



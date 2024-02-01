from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from sysgros.models import User
from sysgros.serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializers = UserSerializer(data= request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Utilisateur introuvable')

        if not user.check_password(password):
            raise AuthenticationFailed('Mot de passe incorrect')

        return Response({
            'message': 'Connexion réussie'
        })



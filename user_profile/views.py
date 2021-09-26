from django.contrib.auth.models import User
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .serializers import UserProfileSerializer


class CreateUserView(views.APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserProfileSerializer(data=data)

        if serializer.is_valid():
            if serializer.validated_data.get('password') != serializer.validated_data.get('password_confirmation'):
                return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer.validated_data.pop('password_confirmation')
            User.objects.create_user(**serializer.validated_data)

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LoginView(ObtainAuthToken):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

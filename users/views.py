from rest_framework import viewsets, views, response, status
from .models import User
from .serializer import UserSerializer, LoginSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class LoginView (views.APIView):
  def post(self, request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return response.Response({"message": "Success login!"}, status=status.HTTP_200_OK)

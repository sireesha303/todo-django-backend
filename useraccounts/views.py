from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ Customized tokenpair view serializer """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    """ Customized tokenpair view """

    serializer_class = MyTokenObtainPairSerializer
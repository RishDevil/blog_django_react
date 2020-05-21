from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView
from articles.models import Article
from .serializers import Articleserializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,  context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'tokens': token.key,
            'user_id': user.username,
            'email': user.email,

        })


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer


class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer


class ArticleDestroyView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = Articleserializer    
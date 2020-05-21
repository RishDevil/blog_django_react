from django.urls import path,include
from django.conf.urls import url
from .views import ArticleListView, ArticleDetailView
from .views import ArticleDestroyView, ArticleUpdateView
from .views import ArticleCreateView, CustomAuthToken
from rest_framework.authtoken import views


urlpatterns = [
    path('', ArticleListView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('<pk>/update/', ArticleUpdateView.as_view()),
    path('<pk>/delete/', ArticleDestroyView.as_view()),
   # url('auth/', CustomAuthToken.as_view()),
     

]

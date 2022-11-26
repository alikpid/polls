from django.urls import path
from . import views
from .views import profile


app_name = 'polls'

urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('register/', views.register, name='register'),
    path('accounts/logout/', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/login', views.BBLoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
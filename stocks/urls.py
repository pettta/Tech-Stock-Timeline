from django.urls import path
from . import views

app_name = 'stocks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:stock_id>/', views.detail, name='detail'),
]
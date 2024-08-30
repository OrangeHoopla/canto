from .views import ItemDetail
from .views import ItemList
from django.urls import path


app_name = 'api'

urlpatterns = [
    path('<int:pk>/', ItemDetail.as_view(), name='detailcreate'),
    path('', ItemList.as_view(), name='listcreate')
]
from django.urls import path
from . import views

urlpatterns = [
    path('api/inventory', views.InventoryItemList.as_view(), name = 'inventory_list'),
    path('api/inventory/<int:pk>', views.InventoryItemDetail.as_view(), name = 'inventory_detail')
]
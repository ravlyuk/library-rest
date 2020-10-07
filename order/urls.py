from django.contrib import admin
from django.urls import path
from .views import *

# order_list = OrderModelViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
#     # 'path': 'partial_update',
#     # 'delete': 'destroy',
# })
#
#
# order = OrderModelViewSet.as_view({
#     'get': 'retrieve',
#     # 'post': 'create',
#     'path': 'partial_update',
#     'delete': 'destroy',
# })
#
# app_name = 'book'
# urlpatterns = [
#     # path('create/', OrderCreateView.as_view()),
#     # path('', OrderAllView.as_view()),
#     # path('<int:pk>/delete/', OrderDeleteView.as_view()),
#     # path('<int:pk>/update/', OrderUpdateView.as_view()),
#     # path('<int:pk>/', OrderGetByIdView.as_view()),
#     path('', order_list),
#     path('<int:pk>/', order),
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', OrderModelViewSet)
urlpatterns = router.urls

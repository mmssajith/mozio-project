from django.urls import path
from .views import *

urlpatterns = [
    path('provider/all', get_all_provider),
    path('provider/<str:name>', get_single_provider),
    path('new-provider/', new_provider),
    path('update/<str:name>', update_single_provider),
    path('delete/<str:name>', delete_single_provider),
    path('<str:name>/delete<int:pk>', delete_single_area),
    path('<str:name>/polygons/<int:pk>', get_single_area),
    path('<str:name>/polygons/all', get_all_area_by_provider),
    path('<str:name>/polygons/create', create_area),
    path('<str:name>/polygons/<int:pk>', update_area),
    path('query', query_data),
]
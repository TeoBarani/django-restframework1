from django.contrib import admin
from django.urls import path
from e_commerce.api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comic_list_api_view/', comic_list_api_view, name='comic_list_api_view'),
    path('comic_retrieve_api_view/', comic_retrieve_api_view, name='comic_retrieve_api_view'),
    path('comic_create_api_view/', comic_create_api_view, name='comic_create_api_view'),
    path('comic_list_filtered_api_view/', comic_list_filtered_api_view, name='comic_list_filtered_api_view'),
    path('comic-title-filter/', comic_retrieve_filtered_api_view),
]
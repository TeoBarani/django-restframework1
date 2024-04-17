from django.contrib import admin
from django.urls import path
from e_commerce.api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comic-list/', comic_list_api_view),
    path('comic-retrieve/', comic_retrieve_api_view),
    path('comic-create/', comic_create_api_view),
    path('comic-list-filter/', comic_list_filtered_api_view),
    path('comic-title-filter/', comic_retrieve_filtered_api_view),
]
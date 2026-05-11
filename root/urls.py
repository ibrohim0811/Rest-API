
from django.contrib import admin
from django.urls import path
from book.views import book, category_child, category_father, parent_category_url, get_all_categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/get-books', book, name="api_getbook"),
    path('api/v1/get-all-categories', get_all_categories, name="api_categories"),
    path('api/v1/get-category_c', category_child, name="api_getcategory"),
    path('api/v1/get-category_f', category_father, name="api_getcategory_f"),
    path('api/v1/get-category/<slug:slug>/', parent_category_url, name="parent_category_url"),

]

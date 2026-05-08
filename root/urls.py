
from django.contrib import admin
from django.urls import path
from book.views import book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/get-books', book, name="api_getbook"),
]

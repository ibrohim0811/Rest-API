from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Category
from .serializer import BookSerializer, CategorySerializer
from django.db import OperationalError



@api_view(['GET', 'POST'])
def book(request):

    if request.method == "GET":
        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":

        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'POST', 'DELETE'])
def get_all_categories(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )    

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
    
    elif request.method == "DELETE":
        category = Category.objects.all()
        category.delete()

        return Response(
            {"message":"Barcha kategoriyalar o'chirildi"},
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET'])
def category_child(request):
    if request.method == "GET":
        
        child = Category.objects.filter(parent__isnull=False).all()
        if child:    
            serializer = CategorySerializer(child, many=True)
            return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
            )
        
        return Response(
            status=status.HTTP_404_NOT_FOUND,
        )   
    
    


@api_view(['GET'])
def category_father(request):
    if request.method == "GET":

        father = Category.objects.filter(parent__isnull=True).all()
        
        if father:
            serializer = CategorySerializer(father, many=True)
        
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
                )
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )



@api_view(['GET'])
def parent_category_url(request, slug):
    try:
        parent_cat = Category.objects.get(name=slug) 
    except Category.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
        

    children = Category.objects.filter(parent=parent_cat)

    if children:
        serializer = CategorySerializer(children, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    else:
        cid = parent_cat.id
        book = Book.objects.filter(category=cid).all()
        serializer = BookSerializer(book, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

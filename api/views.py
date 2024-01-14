from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from lib.models import *
from .serializers import *

# Create your views here.

def home(request):
    return render(request, "home.html")

@api_view(['GET'])
def getBook(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response('Książka została usunięta')

@api_view(['GET'])
def getFriends(request):
    friends = Friend.objects.all()
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addFriend(request):
    serializer = FriendSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getBorrow(request):
    borrows = Borrow.objects.all()
    serializer = BorrowSerializer(borrows, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def BorrowBook(request):
    serializer = BorrowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("books/", views.getBook, name="books"),
    path("add_book/", views.addBook, name = "add_book"),
    path("friends/", views.getFriends, name = "friends"),
    path("borrows/", views.getBorrow, name = "borrows"),
    path("add_friend/", views.addFriend, name="add_friend"),
    path("borrow_book/", views.BorrowBook, name="borrow_book")
]
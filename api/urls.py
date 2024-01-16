from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("books/", views.getBook, name="books"),
    path("add_book/", views.addBook, name = "add_book"),
    path("friends/", views.getFriends, name = "friends"),
    path("borrows/", views.getBorrow, name = "borrows"),
    path("add_friend/", views.addFriend, name="add_friend"),
    path("rm_book/<str:pk>/", views.deleteBook, name="rm_book"),
    path("rm_friend/<str:pk>/", views.deleteFriend, name="rm_friend"),
    path("update_book/<int:pk>/", views.updateBook, name="update_book"),
    path("update_friend/<int:pk>/", views.updateFriend, name="update_friend"),
    path("borrow_book/", views.BorrowBook, name="borrow_book"),
    path("return_book/<int:pk>/", views.ReturnBook, name="return_book"),
]
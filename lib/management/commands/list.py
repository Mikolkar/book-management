from django.core.management.base import BaseCommand, CommandError
from lib.models import Book, Friend, Borrow
import api.api_utils as utls
from api.serializers import *
import json

class Command(BaseCommand):
    help = "Wyświetla listę książek, przyjaciół lub wypożyczeń"

    def add_arguments(self, parser):
        parser.add_argument("type", type=str, choices=["books", "friends", "borrows"])
        parser.add_argument("--api", action="store_true")

    def handle(self, *args, **kwargs):
        list_type = kwargs["type"]
        api_use = kwargs["api"]
        if not api_use:
            if list_type == "books":
                for book in Book.objects.all():
                    self.stdout.write(
                        f"ID: {book.id}, Tytuł: {book.title}, Autor: {book.author}, Rok: {book.year}"
                    )
            elif list_type == "friends":
                for friend in Friend.objects.all():
                    self.stdout.write(
                        f"ID: {friend.id}, Imię: {friend.name}, Email: {friend.email}"
                    )
            elif list_type == "borrows":
                for borrow in Borrow.objects.all():
                    self.stdout.write(
                        f"ID: {borrow.id}, Książka: {borrow.book.title}, Wypożyczający: {borrow.friend.name}, Data wypożyczenia: {borrow.borrow_date}, Data zwrotu: {borrow.return_date}"
                    )
            else:
                raise CommandError(
                    'Nieprawidłowy typ listy. Wybierz "books", "friends" lub "borrows".'
                )

        else:
            if list_type == "books":
                serializer = BookSerializer(Book.objects.all(), many=True)
                print(json.dumps(utls.return_json(serializer.data, "books/"), indent=4))
                
            
            elif list_type == "friends":
                serializer = FriendSerializer(Friend.objects.all(), many=True)
                print(json.dumps(utls.return_json(serializer.data, "friends/"), indent=4))
                    
            elif list_type == "borrows":
                serializer = BorrowSerializer(Borrow.objects.all(), many=True)
                print(json.dumps(utls.return_json(serializer.data, "borrows/"), indent=4))
                
            else:
                return serializer.errors, 400

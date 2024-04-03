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
                        f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}"
                    )
            elif list_type == "friends":
                for friend in Friend.objects.all():
                    self.stdout.write(
                        f"ID: {friend.id}, Name: {friend.name}, Email: {friend.email}"
                    )
            elif list_type == "borrows":
                for borrow in Borrow.objects.all():
                    self.stdout.write(
                        f"ID: {borrow.id}, Book: {borrow.book.title}, Borrower: {borrow.friend.name}, Borrow date: {borrow.borrow_date}, Return date: {borrow.return_date}"
                    )
            else:
                raise CommandError(
                    'Invalid argument. Chose one from the following: "books", "friends" lub "borrows".'
                )
        # Using API
        else:
            self.stdout.write(self.style.SUCCESS("List created by using API."))
            if list_type == "books":
                serializer = BookSerializer(Book.objects.all(), many=True)
                self.stdout.write(
                    json.dumps(utls.return_json(serializer.data, "books/"), indent=4)
                )

            elif list_type == "friends":
                serializer = FriendSerializer(Friend.objects.all(), many=True)
                self.stdout.write(
                    json.dumps(utls.return_json(serializer.data, "friends/"), indent=4)
                )

            elif list_type == "borrows":
                serializer = BorrowSerializer(Borrow.objects.all(), many=True)
                self.stdout.write(
                    json.dumps(utls.return_json(serializer.data, "borrows/"), indent=4)
                )

            else:
                return serializer.errors, 400

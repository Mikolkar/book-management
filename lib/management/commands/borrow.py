from django.core.management.base import BaseCommand, CommandError
from lib.models import Book, Friend, Borrow
from api.api_utils import post_json  # Załóżmy, że masz funkcję post_json w api_utils
from django.core.exceptions import ValidationError
from api.serializers import BorrowSerializer
class Command(BaseCommand):
    help = "Wypożycza książkę znajomemu"

    def add_arguments(self, parser):
        parser.add_argument("book", type=int, help="ID książki do wypożyczenia")
        parser.add_argument("friend", type=int, help="ID znajomego, który wypożycza książkę")
        parser.add_argument("--api", action="store_true", help="Użyj API do wypożyczenia książki")

    def handle(self, *args, **kwargs):
        book_id = kwargs["book"]
        friend_id = kwargs["friend"]
        api_use = kwargs.get("api", False)

        if api_use:
            # Wysyłanie żądania do API
            data={"book": book_id, "friend": friend_id}
            # if serializer.is_valid():
            response = post_json("borrow_book/", data)
            if response.status_code == 200:
                print(f"Book added successfully, data: {response.json()}")
            else:
                print(f"Error: {response.status_code}")
            # else:
            #     print("yolo")
            #     print(serializer.errors)
        else:
            # Logika wypożyczania lokalnego
            try:
                book = Book.objects.get(id=book_id)
                friend = Friend.objects.get(id=friend_id)

                borrow = Borrow(book=book, friend=friend)
                try:
                    borrow.clean()  # Możliwa walidacja
                    borrow.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Książka "{book.title}" została wypożyczona znajomemu {friend.name}.'
                        )
                    )
                except ValidationError as e:
                    raise CommandError(f"Błąd walidacji: {e}")

            except Book.DoesNotExist:
                raise CommandError(f"Książka o ID {book_id} nie istnieje.")
            except Friend.DoesNotExist:
                raise CommandError(f"Znajomy o ID {friend_id} nie istnieje.")

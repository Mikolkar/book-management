from django.core.management.base import BaseCommand, CommandError
from lib.models import Book, Friend, Borrow
from api.api_utils import post_json  
from django.core.exceptions import ValidationError
from api.serializers import BorrowSerializer
from django.utils import timezone
from lib.output import success

@success
class Command(BaseCommand):
    help = "Wypożycza książkę znajomemu"

    def add_arguments(self, parser):
        parser.add_argument("book", type=int, help="ID książki do wypożyczenia")
        parser.add_argument(
            "friend", type=int, help="ID znajomego, który wypożycza książkę"
        )
        parser.add_argument(
            "--api", action="store_true", help="Użyj API do wypożyczenia książki"
        )

    def handle(self, *args, **kwargs):
        book_id = kwargs["book"]
        friend_id = kwargs["friend"]
        api_use = kwargs.get("api", False)

        try:
            book = Book.objects.get(id=book_id)
            friend = Friend.objects.get(id=friend_id)

            if not api_use:
                borrow = Borrow(book=book, friend=friend)
                try:
                    borrow.clean()
                    borrow.save()
                    self.print_success(f'Book "{book.title}" has been borrowed to {friend.name}.')
                    
                except ValidationError as e:
                    raise CommandError(f"Validation error {e}")

            else:
                serializer = BorrowSerializer(
                    data={
                        "book": book_id,
                        "friend": friend_id,
                        "borrow_date": timezone.now().strftime("%Y-%m-%d"),
                    }
                )

                if serializer.is_valid():
                    response = post_json("borrow_book/", serializer.data)

                    if response.status_code == 200:
                        resp = response.json()
                        
                        self.print_success(f"Book {book.title} (id {resp["book"]}) has been borrowed by {friend.name} ({resp["friend"]}) (API).")
                        self.print_success(f"JSON response: {resp}")
                        
                    else:
                        raise CommandError(f"Error: {response.status_code}")
                else:
                    raise CommandError(f"Serializer error: {serializer.errors}")

        except Book.DoesNotExist:
            raise CommandError(f"Book with ID {book_id} does not exist.")
        
        except Friend.DoesNotExist:
            raise CommandError(f"Friend with ID {friend_id} does not exist.")

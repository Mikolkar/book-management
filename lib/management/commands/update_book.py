from django.core.management.base import BaseCommand
from lib.models import Book
from api.serializers import BookSerializer
from api.api_utils import put_json
from lib.output import success


@success
class Command(BaseCommand):
    help = "Aktualizuje książkę w bibliotece na podstawie ID"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int, help="ID książki do aktualizacji")
        parser.add_argument("title", type=str, help="Tytuł książki")
        parser.add_argument("author", type=str, help="Autor książki")
        parser.add_argument("year", type=int, help="Rok wydania książki")
        parser.add_argument("--api", action="store_true")

    def handle(self, *args, **kwargs):
        book_id = kwargs["id"]
        author = kwargs["author"]
        title = kwargs["title"]
        year = kwargs["year"]
        api_use = kwargs["api"]

        if not api_use:
            try:
                book = Book.objects.get(id=book_id)
                book.author = author
                book.title = title
                book.year = year
                book.save()
                self.print_success(f"Book {title} has been updated successfully.")

            except Book.DoesNotExist:
                raise CommandError(f"Book with ID {book_id} does not exist.")

        # Using API
        else:
            serializer = BookSerializer(
                data={"title": title, "author": author, "year": year}
            )
            if serializer.is_valid():
                serialized_data = serializer.validated_data
                response = put_json(f"update_book/{book_id}/", serialized_data)

                if response.status_code == 200:
                    self.print_success(f"Book {response.json()["title"]} (id: {book_id}) has been updated in the database by API.")
                    self.print_success(f"JSON response: {response.json()}")
                    
                else:
                    raise CommandError(f"Error: {response.status_code}")
            else:
                raise CommandError(f"Serializer errors: {serializer.errors}")

from django.core.management.base import BaseCommand
from lib.models import Book
from api.api_utils import *
from api.serializers import BookSerializer
from lib.output import success


@success
class Command(BaseCommand):
    help = "Adds a book to the library"

    def add_arguments(self, parser):
        parser.add_argument("title", type=str)
        parser.add_argument("author", type=str)
        parser.add_argument("year", type=int)
        parser.add_argument("--api", action="store_true")

    def handle(self, *args, **kwargs):
        title = kwargs["title"]
        author = kwargs["author"]
        year = kwargs["year"]
        api_use = kwargs["api"]

        if not api_use:
            if not Book.objects.filter(title=title, author=author, year=year).exists():
                Book.objects.create(title=title, author=author, year=year)

                self.print_success(f"Book {title} has been added to the database.")
            else:
                raise CommandError(f"Book {title} already exists in the database.")

        # Adding book by API
        else:
            serializer = BookSerializer(
                data={"title": title, "author": author, "year": year}
            )

            if serializer.is_valid():
                response = post_json("add_book/", serializer.data)

                if response.status_code == 200:
                    self.print_success(
                        f"Book {response.json()['title']} (id: {response.json()['id']}) has been added to the database by API."
                    )
                    self.print_success(f"JSON response: {response.json()}")
                else:
                    raise CommandError(f"Error: {response.status_code}")

            else:
                return serializer.errors, 400

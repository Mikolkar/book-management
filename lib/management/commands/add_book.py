from django.core.management.base import BaseCommand
from lib.models import Book
from api.api_utils import *
from api.serializers import BookSerializer


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
            Book.objects.create(title=title, author=author, year=year)
            self.stdout.write(
                self.style.SUCCESS(f"Książka {title} dodana do bazy danych")
            )

        else:
            serializer = BookSerializer(
                data={"title": title, "author": author, "year": year}
            )
            if serializer.is_valid():
                response = post_json("add_book/", serializer.data)
                if response.status_code == 200:
                    print(f"Książka dodana do bazy danych, data: {response.json()}")
                else:
                    print(f"Error: {response.status_code}")

            else:
                return serializer.errors, 400

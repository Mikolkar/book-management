from django.core.management.base import BaseCommand
from lib.models import Book, Friend
from api.api_utils import *
from lib.output import success


@success
class Command(BaseCommand):
    help = "Usuwa książkę z bazy danych na podstawie ID"

    def add_arguments(self, parser):
        parser.add_argument("type", type=str, choices=["book", "friend"])
        parser.add_argument("id", type=int)
        parser.add_argument("--api", action="store_true")

    def handle(self, *args, **kwargs):
        lst_type = kwargs["type"]
        id = kwargs["id"]
        api_use = kwargs["api"]

        if not api_use:
            if lst_type == "book":
                try:
                    book = Book.objects.get(id=id)
                    book.delete()
                    self.print_success(f"Book with ID{id} has been deleted.")

                except Book.DoesNotExist:
                    raise CommandError(f"Book with ID {id} does not exist.")

            elif lst_type == "friend":
                try:
                    friend = Friend.objects.get(id=id)
                    friend.delete()
                    self.print_success(
                        f"Friend with ID {id} ({friend.name}) has been deleted."
                    )

                except Friend.DoesNotExist:
                    raise CommandError(f"Friend with ID {id} does not exist.")
            else:
                raise CommandError('Invalid argument. Chose "book" or "friend".')
        else:
            if lst_type == "book":
                response = delete_json(f"rm_book/", id)

                if response.status_code == 200:
                    self.print_success(f"Book with ID {id} has been deleted (API).")
                    self.print_success(f"JSON response: {response.json()}")

                else:
                    raise CommandError(f"Error: {response.status_code}")

            elif lst_type == "friend":
                response = delete_json(f"rm_friend/", id)
                if response.status_code == 200:
                    self.print_success(f"Friend with ID {id} ({response.json()["name"]}) has been deleted (API).")
                    self.print_success(f"JSON response: {response.json()}")

                else:
                    raise CommandError(f"Error: {response.status_code}")

            else:
                return serializer.errors, 400

from django.core.management.base import BaseCommand
from lib.models import Book, Friend
from api.api_utils import *


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
                    self.stdout.write(
                        self.style.SUCCESS(f"Książka o ID {id} została usunięta.")
                    )
                except Book.DoesNotExist:

                    self.stdout.write(
                        self.style.ERROR(f"Książka o ID {id} ({book.title}) nie istnieje.")
                    )

            elif lst_type == "friend":
                try:
                    friend = Friend.objects.get(id=id)
                    friend.delete()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Znajomy o ID {id} ({friend.name}) został usunięty."
                        )
                    )
                except Friend.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Znajomy o ID {id} nie istnieje."))

            else:
                raise CommandError('Nieprawidłowy typ listy. Wybierz "book", "friend".')
        else:
            if lst_type == "book":
                response = delete_json(f"rm_book/", id)
                if response.status_code == 200:
                    print(f"Książka o ID {id} ({response.json()}) została usunięta.")
                    
                else:
                    print(f"Error: {response.status_code}")
                    
            elif lst_type == "friend":
                response = delete_json(f"rm_friend/", id)
                if response.status_code == 200:
                    print(f"Przyjaciek o ID {id} ({response.json()}) został usunięty.")
                    
                else:
                    print(f"Error: {response.status_code}")
                    
            else:
                return serializer.errors, 400 

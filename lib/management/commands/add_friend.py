from django.core.management.base import BaseCommand
from lib.models import Friend
from api.api_utils import *
from api.serializers import FriendSerializer


class Command(BaseCommand):
    help = "Dodaje nowego znajomego do bazy danych"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Imię znajomego")
        parser.add_argument(
            "email",
            type=str,
            help="Email znajomego",
        )
        parser.add_argument("--api", action="store_true")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        email = kwargs["email"]
        api_use = kwargs["api"]

        # Checking if friend already exists
        if not api_use:
            print("Using local database")
            if not Friend.objects.filter(email=email).exists():
                Friend.objects.create(name=name, email=email)
                self.stdout.write(self.style.SUCCESS(f"Dodano znajomego: {name}"))
            else:
                self.stdout.write(
                    self.style.WARNING(f"Znajomy {name} już istnieje w bazie danych.")
                )
        else:
            serializer = FriendSerializer(data={"name": name, "email": email})
            if serializer.is_valid():
                response = post_json("add_friend/", serializer.data)
                if response.status_code == 200:
                    print(f"Znajomy {response.json()} został dodany do bazy danych.")
                else:
                    print(f"Error: {response.status_code}")
            else:
                return serializer.errors, 400

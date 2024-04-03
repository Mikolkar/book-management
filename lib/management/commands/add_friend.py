from django.core.management.base import BaseCommand
from lib.models import Friend
from api.api_utils import *
from api.serializers import FriendSerializer
from lib.output import success


@success
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

        if not api_use:

            # Checking if friend already exists
            if not Friend.objects.filter(email=email).exists():
                Friend.objects.create(name=name, email=email)
                self.print_success(f"Friend {name} has been added to the database.")

            else:
                raise CommandError(
                    f"Friend with email {email} already exists in the database."
                )
        else:
            serializer = FriendSerializer(data={"name": name, "email": email})
            if serializer.is_valid():

                response = post_json("add_friend/", serializer.data)
                if response.status_code == 200:

                    self.print_success(f"Friend {response.json()["name"]} (id: {response.json()["id"]}) has been added to the database by API.")
                    self.print_success(f"JSON response: {response.json()}")
                    
                else:
                    raise CommandError(f"Error: {response.status_code}")
            else:
                return serializer.errors, 400

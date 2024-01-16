from django.core.management.base import BaseCommand
from lib.models import Friend
from api.serializers import FriendSerializer
from api.api_utils import put_json

class Command(BaseCommand):
    help = "Aktualizuje dane znajomego w bazie danych"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int, help="ID znajomego do aktualizacji")
        parser.add_argument("name", type=str, help="Nowe imię znajomego")
        parser.add_argument("email", type=str, help="Nowy email znajomego")
        parser.add_argument("--api", action="store_true")

    def handle(self, *args, **kwargs):
        friend_id = kwargs["id"]
        name = kwargs["name"]
        email = kwargs["email"]
        api_use = kwargs["api"]

        if not api_use:
            try:
                friend = Friend.objects.get(id=friend_id)
                friend.name = name
                friend.email = email
                friend.save()
                self.stdout.write(self.style.SUCCESS(f"Dane znajomego {name} zostały zaktualizowane."))
            except Friend.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Znajomy o ID {friend_id} nie istnieje."))

        else:
            serializer = FriendSerializer(data={"name": name, "email": email})
            if serializer.is_valid():
                serialized_data = serializer.validated_data
                response = put_json(f"update_friend/{friend_id}/", serialized_data)

                if response.status_code == 200:
                    print(f"Dane znajomego zostały zaktualizowane, data: {response.json()}")
                else:
                    print(f"Błąd: {response.status_code}")
            else:
                print(serializer.errors)

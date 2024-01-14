from django.core.management.base import BaseCommand
from lib.models import Friend  


class Command(BaseCommand):
    help = "Dodaje przykładowych znajomych do bazy danych"

    def handle(self, *args, **kwargs):
        friends = Friend.objects.all()

        for friend in friends:
            # Checking if friend already exists
            if not Friend.objects.filter(email=friend["email"]).exists():
                Friend.objects.create(name=friend["name"], email=friend["email"])
                self.stdout.write(
                    self.style.SUCCESS(f'Dodano znajomego: {friend["name"]}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Znajomy {friend["name"]} już istnieje w bazie danych.'
                    )
                )

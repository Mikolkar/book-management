from django.core.management.base import BaseCommand
from lib.models import Borrow
from django.utils import timezone
import datetime
from api.serializers import BorrowSerializer
from api.api_utils import put_json


class Command(BaseCommand):
    help = "Oznacza książkę jako zwróconą"

    def add_arguments(self, parser):
        parser.add_argument("borrow_id", type=int, help="ID wypożyczenia książki")
        parser.add_argument(
            "--return_date",
            type=str,
            help="Data zwrotu (format YYYY-MM-DD)",
            default=timezone.now().strftime("%Y-%m-%d"),
        )
        parser.add_argument("--api", action="store_true", help="Użyj API")

    def handle(self, *args, **kwargs):
        borrow_id = kwargs["borrow_id"]
        return_date = kwargs["return_date"]
        api_use = kwargs["api"]
        try:
            borrow = Borrow.objects.get(id=borrow_id)
            if not api_use:
                borrow.return_date = datetime.datetime.strptime(
                    return_date, "%Y-%m-%d"
                ).date()
                borrow.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Książka "{borrow.book.title}" zwrócona dnia {borrow.return_date}'
                    )
                )

            else:
                return_date = (
                    datetime.datetime.strptime(return_date, "%Y-%m-%d")
                    .date()
                    .isoformat()
                )
                data = {"return_date": return_date}
                api_url = f"return_book/{borrow_id}/"
                response = put_json(api_url, data)

                if response.status_code == 200:
                    print("Książka zwrócona pomyślnie.")
                    print(response.json())
                else:
                    print(f"Błąd: {response.status_code}")

        except Borrow.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f"Wypożyczenie o ID {borrow_id} nie istnieje.")
            )

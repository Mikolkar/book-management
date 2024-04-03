from django.core.management.base import BaseCommand
from lib.models import Borrow
from django.utils import timezone
import datetime
from api.serializers import BorrowSerializer
from api.api_utils import put_json
from lib.output import success


@success
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

            # Not using API
            if not api_use:

                borrow.return_date = datetime.datetime.strptime(
                    return_date, "%Y-%m-%d"
                ).date()
                borrow.save()

                self.print_success(
                    f'Book "{borrow.book.title}" returned on {borrow.return_date}'
                )

            # Using API
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
                    self.print_success(
                        f'Book "{borrow.book.title}" returned successfully (API).'
                    )
                    self.print_success(f"JSON response: {response.json()}")

                else:
                    raise CommandError(f"Error: {response.status_code}")

        except Borrow.DoesNotExist:
            raise CommandError(f"Borrow with ID {borrow_id} does not exist.")

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Opis tego, co robi to polecenie."

    def handle(self, *args, **kwargs):
        self.stdout.write(
            """
add_book - Dodaje książkę do biblioteki, 
wywołanie: add_book <tytuł> <autor> <rok> / --api

add_friend - Dodaje znajomego do biblioteki,
wywołanie: add_friend <imię> <email> / --api

borrow - Wypożycza książkę znajomemu,
wywołanie: borrow <id książki> <id znajomego> / --api

list <books|friends|borrows> - Wyświetla listę książek, znajomych lub wypożyczeń,

rm <book/friend> - Usuwa książkę z biblioteki,
wywołanie: rm <book/friend> <id>  / --api

return - Oznacza książkę jako zwróconą,
wywołanie: return <id wypożyczenia> / --return_date=<date> / --api
    """
        )

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Opis tego, co robi to polecenie."

    def handle(self, *args, **kwargs):
        self.stdout.write(
            """
To use the following commands, first of all, you need to
write python mge.py or poetry run python manage.py before the command. 
for example: python mge.py add_book "title" "author" "year"

To use the API, add --api at the end of the command. 
for example: python mge.py add_book "title" "author" "year" --api

Before this you need to run the server.
python mge.py runserver

Commands:

add_book - Adds a book to the library,
usage: add_book <title> <author> <year> / --api

add_friend - Adds a friend to the library,
usage: add_friend <Name> <email> / --api

borrow - Borrows a book for a friend,
usage: borrow <book id> <friend id> / --api

list - Lists of books, friends, or borrows,
usage: list <books|friends|borrows> - Lists of books, friends, or borrows,

rm <book/friend> - Removes a book or friend from the library,
usage: rm <book/friend> <id> / --api

return - Returns a borrowed book,
usage: return <borrow id> / --return_date=<date> / --api

flush - Removes all data from the database,
usage: flush
    """
        )

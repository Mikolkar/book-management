from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Opis tego, co robi to polecenie."

    def handle(self, *args, **kwargs):
        self.stdout.write(
            """
There are two ways to use these commands.
1.  poetry run <command> <args>
2.  Type once: poetry shell
    and then you can use the commands without poetry run.

for example: 
    (1) poetry run add book "title" "author" "year"
    
    (2) poetry shell
        add book "title" "author" "year"



To use the API, add --api at the end of the command 
but before you need to run the server:
    
for example: 
    poetry run runserver
    poetry run add book "title" "author" "year" --api



Commands:

example_data - Adds example data to the database,
    example_data

add - Adds a book/friend to the library,
    Book:
        add book <title> <author> <year> / --api
    Friend:
        add friend <Name> <email> / --api

borrow - Borrows a book for a friend,
    borrow <book id> <friend id> / --api

list - Lists of books, friends, or borrows,
    list <books/friends/borrows>

remove - Removes a book or friend from the library,
    rm <book/friend> <id> / --api

returnB - Returns a borrowed book,
    returnB <borrow id> / --return_date=<date> / --api

update - Updates a book in the library,
    update <book id> <title> <author> <year> / --api

flush - Removes all data from the database,
    flush
    """
        )

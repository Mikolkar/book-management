from subprocess import run
import sys


# Adding example data to the database
def example_data():
    # Books

    books = [
        ["The Great Gatsby", "F. Scott Fitzgerald", "1925"],
        ["To Kill a Mockingbird", "Harper Lee", "1960"],
        ["1984", "George Orwell", "1949"],
        ["Pride and Prejudice", "Jane Austen", "1813"],
        ["The Catcher in the Rye", "J.D. Salinger", "1951"],
        ["The Hobbit", "J.R.R. Tolkien", "1937"],
        ["The Lord of the Rings", "J.R.R. Tolkien", "1954"],
        ["Animal Farm", "George Orwell", "1945"],
        ["Brave New World", "Aldous Huxley", "1932"],
        ["The Grapes of Wrath", "John Steinbeck", "1939"],
        ["Old man and the sea", "Ernest Hemingway", "1952"],
    ]

    friends = [
        ["Alice", "alice@example.com"],
        ["Bob", "bob@example.com"],
        ["Charlie", "charlie@example.com"],
        ["David", "david@example.com"],
        ["Eve", "eve@example.com"],
        ["Frank", "frank@example.com"],
        ["Grace", "grace@example.com"],
    ]

    # Add books
    for book, author, year in books:
        run(["poetry", "run", "python", "./manage.py", "add_book", book, author, year])

    # Add friends
    for friend, email in friends:
        run(["poetry", "run", "python", "./manage.py", "add_friend", friend, email])

    # Add borrows
    run(["poetry", "run", "python", "./manage.py", "borrow", "1", "1"])
    run(["poetry", "run", "python", "./manage.py", "borrow", "4", "2"])
    run(["poetry", "run", "python", "./manage.py", "borrow", "2", "3"])
    run(["poetry", "run", "python", "./manage.py", "borrow", "6", "1"])


# Returning info about the commands
def info():
    run(["poetry", "run", "python", "./manage.py", "info"])


# Adding a book or a friend to the database
def add():
    args = sys.argv[1:]
    if args[0] == "book":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "add_book",
                    args[1],  # title
                    args[2],  # author
                    args[3],  # year
                    "--api",
                ]
            )
        else:
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "add_book",
                    args[1],  # title
                    args[2],  # author
                    args[3],  # year
                ]
            )
    elif args[0] == "friend":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "add_friend",
                    args[1],  # name
                    args[2],  # email
                    "--api",
                ]
            )
        else:
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "add_friend",
                    args[1],  # name
                    args[2],  # email
                ]
            )


# Returning list of books, friends or borrows
def lst():
    args = sys.argv[1:]
    run(["poetry", "run", "python", "./manage.py", "list", args[0]])


# Running the server
def runserver():
    run(["poetry", "run", "python", "./manage.py", "runserver"])


# Borrowing a book for a friend
def borrow():
    args = sys.argv[1:]
    if args[-1] == "--api":
        run(
            [
                "poetry",
                "run",
                "python",
                "./manage.py",
                "borrow",
                args[0],  # book id
                args[1],  # friend id
                "--api",
            ]
        )
    else:
        run(
            [
                "poetry",
                "run",
                "python",
                "./manage.py",
                "borrow",
                args[0],  # book id
                args[1],  # friend id
            ]
        )


# Returning a borrowed book
def ret():
    args = sys.argv[1:]
    if args[-1] == "--api":
        run(
            [
                "poetry",
                "run",
                "python",
                "./manage.py",
                "return",
                args[0],  # borrow id
                "--api",
            ]
        )
    else:
        run(
            [
                "poetry",
                "run",
                "python",
                "./manage.py",
                "return",
                args[0],  # borrow id
            ]
        )


# Removing a book or a friend from the database
def remove():
    args = sys.argv[1:]
    if args[-1] == "--api":
        run(
            [
                "poetry",
                "run",
                "python",
                "./manage.py",
                "rm",
                args[0],  # book/friend
                args[1],  # id
                "--api",
            ]
        )
    else:
        run(
            [
                "poetry",
                "run",
                "python",
                "./manage.py",
                "rm",
                args[0],  # book/friend
                args[1],  # id
            ]
        )


# Removing all data from the database
def flush():
    run(["poetry", "run", "python", "./manage.py", "flush"])


# Updating a book or a friend in the database
def update():
    args = sys.argv[1:]
    if args[0] == "book":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "update_book",
                    args[1],  # book id
                    args[2],  # title
                    args[3],  # author
                    args[4],  # year
                    "--api",
                ]
            )
        else:
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "update_book",
                    args[1],  # book id
                    args[2],  # title
                    args[3],  # author
                    args[4],  # year
                ]
            )
    elif args[0] == "friend":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "update_friend",
                    args[1],  # friend id
                    args[2],  # name
                    args[3],  # email
                    "--api",
                ]
            )
        else:
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "update_friend",
                    args[1],  # friend id
                    args[2],  # name
                    args[3],  # email
                ]
            )
    else:
        throw("Invalid argument")

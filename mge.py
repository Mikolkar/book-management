from subprocess import run
import sys


def expample_data():
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


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "info":
        run(["poetry", "run", "python", "./manage.py", "info"])

    elif args[0] == "runserver":
        run(["poetry", "run", "python", "./manage.py", "runserver"])

    elif args[0] == "list":
        run(["poetry", "run", "python", "./manage.py", "list", args[1]])

    elif args[0] == "add_book":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "add_book",
                    args[1],
                    args[2],
                    args[3],
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
                    args[1],
                    args[2],
                    args[3],
                ]
            )
    elif args[0] == "add_friend":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "add_friend",
                    args[1],
                    args[2],
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
                    args[1],
                    args[2],
                ]
            )
    elif args[0] == "borrow":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "borrow",
                    args[1],
                    args[2],
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
                    args[1],
                    args[2],
                ]
            )
    elif args[0] == "return":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "return",
                    args[1],
                    args[2],
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
                    args[1],
                    args[2],
                ]
            )
    elif args[0] == "rm":
        if args[-1] == "--api":
            run(
                [
                    "poetry",
                    "run",
                    "python",
                    "./manage.py",
                    "rm",
                    args[1],
                    args[2],
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
                    args[1],
                    args[2],
                ]
            )
    elif args[0] == "example_data":
        expample_data()

    elif args[0] == "flush":
        run(["poetry", "run", "python", "./manage.py", "flush"])

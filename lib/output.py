def success(cls):
    def print_success(self, text):
        self.stdout.write(self.style.SUCCESS(text))

    cls.print_success = print_success
    return cls

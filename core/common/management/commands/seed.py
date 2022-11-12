from django.core.management import BaseCommand


class Command(BaseCommand):
    help: str = "Generate fake data and seed the models with them, default are 10"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--amount", type=int, help="The amount of fake data you want")

    def handle(self, *args, **options):
        amount = options.get("amount", 10)
        print(amount)

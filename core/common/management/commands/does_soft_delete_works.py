from django.core.management.base import BaseCommand
from core.watchlist.models import Movie


class Command(BaseCommand):
    """
    Testing if soft delete with query manager works
    """

    def handle(self, *args, **options):
        qs = Movie.objects.filter()
        print(qs.query)

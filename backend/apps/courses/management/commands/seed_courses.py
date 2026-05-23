from django.core.management.base import BaseCommand
from seed.scripts.seed_courses import run


class Command(BaseCommand):
    help = "Seed courses data"

    def handle(self, *args, **kwargs):
        run()
        self.stdout.write(self.style.SUCCESS("Seeding completed"))
from django.core.management.base import BaseCommand
from hits.models import Hit, Artist
from datetime import datetime


class Command(BaseCommand):
    help = "Populates the database with initial hits and artists"

    def handle(self, *args, **kwargs):
        artists = [
            Artist.objects.create(first_name="Vincent", last_name="Belorgey"),
            Artist.objects.create(first_name="Travis", last_name="Scott"),
            Artist.objects.create(first_name="Lalisa", last_name="Manobal"),
            Artist.objects.create(first_name="Chloe", last_name="Breez"),
        ]

        songs_by_artist = {
            artists[0]: [
                "Nightcall",
                "Roadgame",
                "Odd Look",
                "Renegade",
                "Pacific Coast Highway",
            ],
            artists[1]: [
                "Goosebumps",
                "SICKO MODE",
                "Trance",
                "HIGHEST IN THE ROOM",
                "MY EYES",
            ],
            artists[2]: ["Born Again", "Rockstar", "New Woman", "LALISA", "MONEY"],
            artists[3]: [
                "Unholy",
                "Hell's Comin With Me",
                "Good Luck Babe",
                "Save a Horse Ride a Cowgirl",
                "Livin La Vida Loca",
            ],
        }

        for artist, songs in songs_by_artist.items():
            for song in songs:
                Hit.objects.create(
                    title=song,
                    artist=artist,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )

        self.stdout.write(self.style.SUCCESS("Successfully populated the database!"))

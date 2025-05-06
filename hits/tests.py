from django.test import TestCase, Client
from hits.models import Artist, Hit


class HitAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = Artist.objects.create(first_name="Test", last_name="Artist")
        self.hit = Hit.objects.create(title="Test Song", artist=self.artist)

    def test_get_hits(self):
        response = self.client.get("/api/v1/hits/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0].get("title"), self.hit.title)
        self.assertEqual(response.json()[0].get("artist"), str(self.artist))

    def test_create_hit(self):
        data = {"title": "New Song", "artist_id": self.artist.id}
        response = self.client.post(
            "/api/v1/hits/", data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get("title"), "New Song")

    def test_get_hit_detail(self):
        response = self.client.get(f"/api/v1/hits/{self.hit.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("title"), self.hit.title)

    def test_update_hit(self):
        data = {"title": "Updated Song"}
        response = self.client.put(
            f"/api/v1/hits/{self.hit.id}/",
            data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("title"), "Updated Song")

    def test_delete_hit(self):
        response = self.client.delete(f"/api/v1/hits/{self.hit.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Hit.objects.filter(id=self.hit.id).exists())

    def test_get_artists(self):
        response = self.client.get("/api/v1/artists/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0].get("id"), self.artist.id)
        self.assertEqual(response.json()[0].get("first_name"), self.artist.first_name)
        self.assertEqual(response.json()[0].get("last_name"), self.artist.last_name)

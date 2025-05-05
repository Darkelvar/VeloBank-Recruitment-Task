from django.http import JsonResponse
from django.views import View
from hits.models import Hit, Artist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


@method_decorator(csrf_exempt, name="dispatch")
class HitListCreate(View):
    def get(self, request):
        hits = Hit.objects.all().order_by("-created_at")[:20]
        hits_data = [
            {
                "title": hit.title,
                "artist": str(hit.artist),
                "title_url": hit.id,  # expose the automatic `id` as `title_url`
                "created_at": hit.created_at,
                "updated_at": hit.updated_at,
            }
            for hit in hits
        ]
        return JsonResponse(hits_data, safe=False, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            artist = Artist.objects.get(id=data["artist_id"])
            title = data["title"]
            hit = Hit.objects.create(title=title, artist=artist)
            return JsonResponse(
                {
                    "title": hit.title,
                    "artist": str(hit.artist),
                    "title_url": hit.id,
                    "created_at": hit.created_at,
                },
                status=201,
            )
        except Artist.DoesNotExist:
            return JsonResponse({"error": "Artist not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class HitDetailUpdateDelete(View):
    def get(self, request, title_url):
        try:
            hit = Hit.objects.get(id=title_url)
            hit_data = {
                "title": hit.title,
                "artist": str(hit.artist),
                "title_url": hit.id,
                "created_at": hit.created_at,
                "updated_at": hit.updated_at,
            }
            return JsonResponse(hit_data, status=200)
        except Hit.DoesNotExist:
            return JsonResponse({"error": "Hit not found"}, status=404)

    def put(self, request, title_url):
        try:
            data = json.loads(request.body)
            hit = Hit.objects.get(id=title_url)
            if "title" in data:
                hit.title = data["title"]
            if "artist_id" in data:
                hit.artist = Artist.objects.get(id=data["artist_id"])
            hit.updated_at = None  # force refresh
            hit.save()
            return JsonResponse(
                {
                    "id": hit.id,
                    "title": hit.title,
                    "artist": str(hit.artist),
                    "title_url": hit.id,
                    "created_at": hit.created_at,
                    "updated_at": hit.updated_at,
                },
                status=200,
            )
        except Artist.DoesNotExist:
            return JsonResponse({"error": "Artist not found"}, status=404)
        except Hit.DoesNotExist:
            return JsonResponse({"error": "Hit not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, title_url):
        try:
            hit = Hit.objects.get(id=title_url)
            hit.delete()
            return JsonResponse({}, status=204)
        except Hit.DoesNotExist:
            return JsonResponse({"error": "Hit not found"}, status=404)

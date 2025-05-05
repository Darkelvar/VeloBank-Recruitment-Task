from django.contrib import admin
from django.urls import path
from hits import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/hits", views.HitListCreate.as_view(), name="hit-list"),
    path(
        "api/v1/hits/<int:title_url>",
        views.HitDetailUpdateDelete.as_view(),
        name="hit-detail",
    ),
]

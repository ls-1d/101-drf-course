from django.urls import path

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (
    WatchDetailAV,
    WatchListAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
)

urlpatterns = [
    path("", WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream"),
    path(
        "stream/<int:pk>/",
        StreamPlatformDetailAV.as_view(),
        name="streamplatform-detail",
    ),
]

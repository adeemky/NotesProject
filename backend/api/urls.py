from django.urls import path
from api.views import NoteListCreateView, NoteDeleteView


urlpatterns = [
    path("notes/", NoteListCreateView.as_view(), name="notes"),
    path("note/delete/<int:pk>/", NoteDeleteView.as_view(), name="delete-note"),
]

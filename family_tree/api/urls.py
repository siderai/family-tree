from django.urls import path

from family_tree.api import views


urlpatterns = [
    path("v1/people/", views.HumanCreateView.as_view()),
    path("v1/people/<int:pk>/", views.HumanReadUpdateView.as_view()),
    path("v1/people/<int:pk>/ancestors/", views.HumanAncestorsView.as_view()),
]

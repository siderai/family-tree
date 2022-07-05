from django.urls import path

from family_tree.api import views


urlpatterns = [
    path("v1/people/", views.HumanCreateView.as_view()),
    path("v1/people/<int:pk>/", views.HumanReadUpdateView.as_view()),
    path("v1/people/<int:pk>/ancestors/", views.HumanAncestorsView.as_view()),
]


# from rest_framework import routers

# from entities import api_views as ApiViews

# router = routers.DefaultRouter()
# router.register(r'groups/', ApiViews.GroupViewSet)
# router.register(r'users/', ApiViews.UserViewSet)

# urlpatterns = [
#     path('admin', admin.site.urls),
#     path('api/v0/', include(router.urls)),
# ]

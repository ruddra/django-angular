from movies.views import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
urlpatterns = router.urls

from .views import *

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'drivers', DriverAPI)
router.register(r'vehicles', VehicleAPI)
router.register(r'trips', TripAPI)
router.register(r'locations', LocationAPI)

urlpatterns = router.urls

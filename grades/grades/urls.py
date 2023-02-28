from django.urls import path, include
from rest_framework import routers
from api.views import StudentViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('students_api/', include(router.urls)),
    path('admin/', admin.site.urls),

]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
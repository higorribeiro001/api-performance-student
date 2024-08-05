from rest_framework.routers import SimpleRouter
from .views import *

app_name = 'student-performance'
student_performance_api_v1_router = SimpleRouter()

student_performance_api_v1_router.register(
    'api/v1',
    StudentPerformanceView,
    basename='student-performance-api'
)

urlpatterns = student_performance_api_v1_router.urls
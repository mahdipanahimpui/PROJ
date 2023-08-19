from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'tutorials'

urlpatterns = [

]


course_router = routers.SimpleRouter()
course_router.register('courses', views.CourseViewSet, basename='courses') # url, view name
urlpatterns += course_router.urls 


take_course_router = routers.SimpleRouter()
take_course_router.register('takecourses', views.TakeCourseViewSet, basename='takecourses') # url, view name
urlpatterns += take_course_router.urls 
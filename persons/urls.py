from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'persons'

urlpatterns = [
    path('', views.PersonView.as_view(), name='all_persons'),
    path('<int:pk>/', views.PersonView.as_view(), name='get_person'),
]


edu_router = routers.SimpleRouter()
edu_router.register('edus', views.EducationViewSet, basename='edus') # url, view name
urlpatterns += edu_router.urls 



field_router = routers.SimpleRouter()
field_router.register('fields', views.FieldViewSet, basename='fields')
urlpatterns += field_router.urls


participant_router = routers.SimpleRouter()
participant_router.register('participants', views.ParticipantViewSet, basename='participants')
urlpatterns += participant_router.urls


teacher_router = routers.SimpleRouter()
teacher_router.register('teachers', views.TeacherViewSet, basename='techaers')
urlpatterns += teacher_router.urls



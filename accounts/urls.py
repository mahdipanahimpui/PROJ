from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'accounts'

urlpatterns = [
    # path('', views.CreateUserView.as_view(), name='create_user')
    # path('', include(router.urls)),

]


router = routers.SimpleRouter()
router.register('users', views.UserViewSet, basename='users') # url, view name
urlpatterns += router.urls 
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router=DefaultRouter()
router.register('hello-vieswet',views.HelloViewSets,base_name='hello-viewset')
#we have provided the query set for UserProfileViewset, hence we dont have set up a base name here
router.register('profile',views.UserprofileViewSet)

urlpatterns=[
    path('hello-view/',views.HelloApiview.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

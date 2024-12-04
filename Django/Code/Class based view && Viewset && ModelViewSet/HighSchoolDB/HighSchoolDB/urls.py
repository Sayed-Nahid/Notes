#code for viewset && ModelViewset  video number 16, 17
from django.contrib import admin
from django.urls import path, include
from highschoolAPI import views
from rest_framework.routers import DefaultRouter

#Router object
router = DefaultRouter()

#Register StudentViewSet with Router
router.register('studentinfo', views.StudentModelViewSet, basename='student')             #for viewset      router.register('studentinfo', views.StudentViewSet, basename='student')
#For ReadOnlyModelViewSet      router.register('studentinfo', views.StudentReadOnlyModelViewSet, basename='student')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]








"""
Code for class based view


from django.contrib import admin
from django.urls import path
from highschoolAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/', views.StudentAPI.as_view()),
    path('student_info/<int:pk>/', views.StudentAPI.as_view())
    #path('student_info/', views.StudentInfo.as_view())
]
"""
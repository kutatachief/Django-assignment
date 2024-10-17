from django.urls import path
from .views import cohort_home, about_cohort

urlpatterns = [
    path('',cohort_home,name='studenthome' ),
    path('studentabout/',about_cohort, name='studentabout')
    

]
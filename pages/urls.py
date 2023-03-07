from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='root'),
    path('news/', HomeView.as_view(), name='news'),
    path('news/recent/', HomeView.as_view(), name='recent'),
    path('news/archive/', HomeView.as_view(), name='archive'),
    path('news/archive/package-1/', HomeView.as_view(), name='package-1'),
    path('news/archive/package-1/subpackage-1', HomeView.as_view(), name='subpackage-1'),
    path('news/archive/package-2/', HomeView.as_view(), name='package-2'),
    path('dev/', HomeView.as_view(),  name='dev'),
    path('dev/monitoring/', HomeView.as_view(),  name='monitoring'),
    path('dev/monitoring/servers/', HomeView.as_view(),  name='servers'),
    path('projects/', HomeView.as_view(),  name='projects'),
    path('projects/current/', HomeView.as_view(),  name='current'),
    path('projects/current/project-1/', HomeView.as_view(),  name='project-1'),
    path('projects/current/project-1/subitem-1-1/', HomeView.as_view(),  name='subitem-1-1'),
    path('projects/current/project-1/subitem-1-2/', HomeView.as_view(),  name='subitem-1-2'),
    path('projects/current/project-2/', HomeView.as_view(),  name='project-2'),
    path('projects/current/project-3/', HomeView.as_view(),  name='project-3'),
    path('projects/current/project-3/subitem-3-1/', HomeView.as_view(),  name='subitem-3-1'),
    path('contacts/', HomeView.as_view(),  name='contacts'),
    path('contacts/info/', HomeView.as_view(),  name='info'),
    path('contacts/location/', HomeView.as_view(),  name='location'),

]

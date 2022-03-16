from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    
    path('project/review/<project_id>',views.project_review,name='project_review'),
    path('search/',views.search_project, name='search_results'),
    path('new/project',views.new_project,name='new-project'),
    path('profile/',views.profile,name='profile'),
    path('new_profile/',views.new_profile,name = 'new_profile'),
    path('edit/profile/',views.profile_edit,name = 'edit_profile'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
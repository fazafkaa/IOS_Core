from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.finder,
        name="finder"
    ),

    path(
        "folder/<int:folder_id>/",
        views.folder_detail,
        name="folder_detail"
    ),

    path(
        "portfolio/",
        views.portfolio,
        name="portfolio"
    ),

    path(
        "project/<int:file_id>/",
        views.project_detail,
        name="project_detail"
    ),

]
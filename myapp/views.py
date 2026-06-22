from django.shortcuts import render, get_object_or_404

from .models import Folder, File, Profile

def get_breadcrumb(folder):

    breadcrumbs = []

    current = folder

    while current:

        breadcrumbs.insert(0, current)

        current = current.parent

    return breadcrumbs

def get_sidebar_folders():

    return Folder.objects.filter(
        parent=None
    )


def finder(request):

    folders = Folder.objects.filter(
        parent=None
    )

    return render(
    request,
    "finder.html",
    {
        "folders": folders,
        "sidebar_folders": folders,
        "current_folder": None
    }
)

def folder_detail(request, folder_id):

    folder = get_object_or_404(
        Folder,
        id=folder_id
    )

    children = folder.children.all()

    files = folder.files.all()
    return render(
    request,
    "pages/folder_detail.html",
    {
        "folder": folder,
        "children": children,
        "files": files,
        "breadcrumbs": get_breadcrumb(folder),
        "sidebar_folders": get_sidebar_folders(),
        "current_folder": get_root_folder(folder)
    }
)

def project_detail(request, file_id):

    file = get_object_or_404(
        File,
        id=file_id
    )

    return render(
    request,
    "pages/project_detail.html",
    {
        "file": file,
        "folder": file.folder,
        "breadcrumbs": get_breadcrumb(file.folder),
        "sidebar_folders": get_sidebar_folders(),
        "current_folder": get_root_folder(file.folder)
    }
)

def profile(request):

    profile = Profile.objects.first()

    return render(
        request,
        "pages/profile.html",
        {
            "profile": profile,
            "sidebar_folders": get_sidebar_folders()
        }
    )


def portfolio(request):

    return render(
        request,
        "pages/portfolio.html",
        {
            "sidebar_folders": get_sidebar_folders()
        }
    )


def photo(request):
    return render(request, "pages/photo.html")


def about(request):
    return render(request, "pages/about.html")


def education(request):
    return render(request, "pages/education.html")


def skills(request):
    return render(request, "pages/skills.html")


def software(request):
    return render(request, "pages/software.html")


def resume(request):
    return render(request, "pages/resume.html")


def contact(request):
    return render(request, "pages/contact.html")

def get_root_folder(folder):

    current = folder

    while current.parent:
        current = current.parent

    return current
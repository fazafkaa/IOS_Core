from django.shortcuts import render
from .models import Folder
from django.shortcuts import get_object_or_404

def finder(request):

    folders = Folder.objects.filter(
        parent=None
    )

    context = {
        "folders": folders
    }

    return render(
        request,
        "finder.html",
        context
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


# def portfolio(request):
#     return render(request, "pages/portfolio.html")

from .models import Folder, File


def portfolio(request):

    branding = Folder.objects.get(name="Branding")

    files = File.objects.filter(folder=branding)

    context = {
        "files": files
    }

    return render(
        request,
        "pages/portfolio.html",
        context
    )

def resume(request):
    return render(request, "pages/resume.html")


def contact(request):
    return render(request, "pages/contact.html")

def folder_detail(request, folder_id):

    folder = Folder.objects.get(
        id=folder_id
    )

    children = folder.children.all()

    files = folder.files.all()

    context = {
        "folder": folder,
        "children": children,
        "files": files,
    }

    return render(
        request,
        "pages/folder_detail.html",
        context
    )

def project_detail(request, file_id):

    file = get_object_or_404(
        File,
        id=file_id
    )

    context = {
        "file": file
    }

    return render(
        request,
        "pages/project_detail.html",
        context
    )
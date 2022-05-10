from django.shortcuts import render, get_object_or_404
from certificates.models import Certificate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Create your views here.
def all_certificates(request):
    #query the db to return all project objects
    certificates = Certificate.objects.all()
    return render(request, 'certificates/all_certificates.html',
                  {'certificates': certificates})

def certificate_detail(request, pk):
    certificates = Certificate.objects.get(pk=pk)
    return render(request, 'certificates/certificate_detail.html',
                  {'certificates': certificates})

def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:

        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")

def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")

@login_required
def private_place(request):
    return HttpResponse("Shhh, members only!", content_type="text/plain")

@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")

@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, "DANGER WILL ROBINSON")

    return HttpResponse("Messages added", content_type="text/plain")
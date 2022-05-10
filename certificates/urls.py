from django.contrib import admin
from django.urls import path, include
from certificates import views

# do I need to add the part 3 urls to portfolio.urls?

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.all_certificates, name="all_certificates"),
    path("certificate_detail/<int:pk>", views.certificate_detail, name="certificate_detail"),
    path("see_request/", views.see_request, name='see_request'),
    path("user_info/", views.user_info, name='user_info'),
    path("private_place/", views.private_place),
    path("accounts/", include("django.contrib.auth.urls")),
    path("staff_place/", views.staff_place),
    path("add_messages/", views.add_messages),
]
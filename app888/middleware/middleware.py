from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class AuthMD(MiddlewareMixin):

    def process_request(self, request):

        if request.path_info in [reverse("login")]:
            return

        if request.path_info.startswith("/admin/"):
            return

        print(request.session.get("is_login"))
        if not request.session.get("is_login"):
            return redirect("login")





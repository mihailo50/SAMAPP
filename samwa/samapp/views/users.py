from django.contrib.auth import authenticate, login as auth_login

from django.shortcuts import render, redirect

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            auth_login(request, user)
            return redirect("homepage")
        else:
            error_message = "Invalid username or password."
    else:
        error_message = None

    context = {
        "error_message": error_message,
    }

    return render(request, "login/login_page.html", context)

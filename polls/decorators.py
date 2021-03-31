# decorators are mainly used here to make the CODE CLEANER and
# to handle stuff like not allowing logged in users to
# go back to the sign up/ log in pages and restrict access for any views in any way we may need

from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('polls:home')
        return view_func(request, *args, **kwargs)

    return wrapper_func

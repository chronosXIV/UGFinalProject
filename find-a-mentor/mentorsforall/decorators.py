from django.http import HttpResponseBadRequest
from .models import Profile, Account

def profile(f):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseBadRequest('Invalid user')
        p = Profile.objects.get(accountid=request.user)

        request.profile = p
        return f(request, *args, **kwargs)
    return wrapper

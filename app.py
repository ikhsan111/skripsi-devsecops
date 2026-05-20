from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Rule CSRF SonarQube akan langsung mendeteksi decorator ini
@csrf_exempt
def my_view(request):
    return HttpResponse("CSRF protection is disabled!")
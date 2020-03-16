from django.http import HttpResponse
def wish(request):
    message="hello jai"
    return HttpResponse(message)

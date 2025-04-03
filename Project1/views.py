from django.http import HttpResponse
def homepage(request):  
  return HttpResponse("welcome to BP store")


def aboutus(request):
  return HttpResponse("About Us")
def contact(request):
  return HttpResponse("Contact")
def services(request):
  return HttpResponse("Services")

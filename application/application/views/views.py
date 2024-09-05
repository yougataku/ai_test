from django.http import HttpResponse

def home_view(request):
    return HttpResponse("ホームページ")

def contact_view(request):
    return HttpResponse("連絡先ページ")

def services_view(request):
    return HttpResponse("サービスページ")
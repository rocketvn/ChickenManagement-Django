from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')


# def Home(request):
#         return render(request, 'homepage/User.html')

def base(request):
        return render(request, 'homepage/base.html')

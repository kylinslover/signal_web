from django.shortcuts import render, HttpResponse


# Create your views here.

def show_fileter(request):
    return render(request, "filter/filter_show.html")

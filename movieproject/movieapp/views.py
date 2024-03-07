from django.shortcuts import render
from django.urls import reverse_lazy

from movieapp.models import Movietb

from movieapp.form import movieform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

# def home(request):
#     m = Movietb.objects.all()
#     return render(request, 'home.html', {'m': m})

class MovieList(ListView):  # ListView displays all objects/records retrieving from a model.
    model = Movietb
    template_name = "home.html"
    context_object_name = "m"


# def details(request, p):
#     m = Movietb.objects.get(id=p)
#     return render(request, 'details.html', {'m': m})


class MovieDetail(DetailView):  # DetailView diaplays a particular object retrieving from model.
    model = Movietb
    template_name = 'details.html'
    context_object_name = "m"


# def add(request):
#     if (request.method == "POST"):
#         form = movieform(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#     form = movieform()
#     return render(request, 'add.html', {'form': form})

class Movieadd(CreateView):  # CreateView displays a form for adding new object and handles form
    model = Movietb
    template_name = "add.html"
    fields = "__all__"
    success_url = reverse_lazy('movieapp:home')


# def update(request, p):
#     m = Movietb.objects.get(id=p)
#     if (request.method == "POST"):
#         form = movieform(request.POST, request.FILES, instance=m)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#     form = movieform(instance=m)
#     return render(request, 'update.html', {'form': form})

class MovieUpdate(UpdateView):
    model = Movietb
    template_name = "update.html"
    fields = "__all__"
    success_url = reverse_lazy('movieapp:home')


# def delete(request, p):
#     m = Movietb.objects.get(id=p)
#     m.delete()
#     return home(request)


class Moviedelete(DeleteView):
    model = Movietb
    success_url = reverse_lazy('movieapp:home')
    template_name = 'delete.html'

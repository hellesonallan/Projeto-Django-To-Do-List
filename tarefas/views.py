from datetime import date

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Tarefas

class TarefasView(ListView):
    model = Tarefas

class TarefasCreateView(CreateView):
    model = Tarefas
    fields = ["titulo", "data_final"]
    success_url = reverse_lazy("tarefas_list")

class TarefasUpdateView(UpdateView):
    model = Tarefas
    fields = ["titulo", "data_final"]
    success_url = reverse_lazy("tarefas_list")

class TarefasDeleteView(DeleteView):
    model = Tarefas
    success_url = reverse_lazy("tarefas_list")

class TarefasFinishView(View):
    def get(self, request, pk):
        tarefas = get_object_or_404(Tarefas, pk=pk)
        tarefas.marque_como_finalizado()
        return redirect("tarefas_list")
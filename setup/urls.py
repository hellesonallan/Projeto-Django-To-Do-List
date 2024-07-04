from django.contrib import admin
from django.urls import path

from tarefas.views import TarefasView, TarefasCreateView, TarefasUpdateView, TarefasDeleteView, TarefasFinishView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TarefasView.as_view(), name="tarefas_list"),
    path("create", TarefasCreateView.as_view(), name="tarefas_create"),
    path("update/<int:pk>", TarefasUpdateView.as_view(), name="tarefas_update"),
    path("delete/<int:pk>", TarefasDeleteView.as_view(), name="tarefas_delete"),
    path("finished/<int:pk>", TarefasFinishView.as_view(), name="tarefas_finish"),
]

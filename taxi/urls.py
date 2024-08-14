from django.urls import path

from .views import index, ManufacturerListView

urlpatterns = [
    path("", index, name="index"),
    path("", ManufacturerListView.as_view(), name="manufacture_list_view")
]

app_name = "taxi"

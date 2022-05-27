from django.urls import path
from .views import ArticuloApiView, DeleteArticuloView, RetrieveArticulosView, UploadArticuloImage, UpdateArticuloView

urlpatterns = [
    path('articulo/', ArticuloApiView.as_view()),
    path('articulo/<int:pk>', RetrieveArticulosView.as_view()),
    path('articulo/delete/<int:pk>', DeleteArticuloView.as_view()),
    path('articulo/update/<int:pk>', UpdateArticuloView.as_view()),
    path('articulo/upload', UploadArticuloImage.as_view()),
    
    
]
from django.urls import path # type: ignore
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea , Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView # type: ignore



urlpatterns = [path('', ListaPendientes.as_view(), name='main'),
               path('login/', Logueo.as_view(), name='Login'),
               path('registro/', PaginaRegistro.as_view(),name='Registro'),
               path('logout/',LogoutView.as_view(next_page='Login'), name='Logout'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('NuevaTarea/', CrearTarea.as_view(), name='NuevaTarea'),
               path('EditarTarea/<int:pk>', EditarTarea.as_view(), name='EditarTarea'),
               path('EliminarTarea/<int:pk>', EliminarTarea.as_view(), name='EliminarTarea')]
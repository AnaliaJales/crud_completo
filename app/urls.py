from django.conf import settings
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from .views import CadastroDetail, CadastroList, CadastroCreate, CadastroUpdate, CadastroDelete
 
app_name = 'app'

urlpatterns = [
    path('', CadastroList.as_view(), name='cadastro_list'),
    path('create/', CadastroCreate.as_view(), name='cadastro_create'),
    path('update/<int:pk>/', CadastroUpdate.as_view(), name='cadastro_update'),
    path('detail/<int:pk>/', CadastroDetail.as_view(), name='cadastro_detail'),
    path('delete/<int:pk>/', CadastroDelete.as_view(), name='cadastro_delete'),
]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
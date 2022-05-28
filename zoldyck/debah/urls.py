from django.urls import include, re_path,path
from . import views


app_name = 'debah'
urlpatterns = [
    path("list", views.list_abt , name="list_abt"),
    path("add_deba7",views.add_deba7,name='ajouter'),
   # path("association/<int:d_id>" ,views.association , name="association"),
    path("association/association_org/<int:req_id>" , views.association_org, name="association_org"),
    path("association/edit/<int:abt_id>" ,views.edit , name="edit"),
    path("association/delete/<int:abt_id>" ,views.delete , name="delete"),

    


    ]

from django.urls import path,include
from .import views
urlpatterns = [
  path('',views.Create,name='Create'),
  path('login',views.userlogin,name='userlogin'),
  path('Table',views.Table,name='Table'),
  path('Reg',views.Registration,name='Reg'),
  path('Change',views.Change,name='Change'),
  path('delete/<int:s_id>',views.delete,name='delete'),
  path('Change/<int:s_id>',views.Change,name='Change'),
  path('logout',views.userlogout,name="userlogout"),

]


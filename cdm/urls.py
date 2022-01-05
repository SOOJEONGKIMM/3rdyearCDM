from django.urls import path

import anam_cdm_v5
#from anam_cdm_v5 import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from cdm import views

urlpatterns = [
	#path('',views.index, name='index'),
	#path('admin/',admin.site.urls),
	path('main',views.Main),
	#path('anam_cdm_v5/',include('anam_cdm_v5')),
	path('list', views.Condition_Occurr),
	path('death',views.Death),
	path('person',views.Person),
	#path('update',views.UpdateFunc),
	#path('updateok',views.UpdateFuncOk),

]

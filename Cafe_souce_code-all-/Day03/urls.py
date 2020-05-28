from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="index"),
    path('myapp/create', myapp.views.create, name="create"),
    path('myapp/create_pro', myapp.views.create_pro, name="create_pro"),
    path('myapp/show', myapp.views.show, name="show"),
    path('myapp/updateSearch', myapp.views.updateSearch, name="updateSearch"),
    path('myapp/search', myapp.views.search, name="search"),
    path('myapp/update', myapp.views.update, name="update"),
    path('myapp/deleteSearch', myapp.views.deleteSearch, name="deleteSearch"),
    path('myapp/find', myapp.views.find, name="find"),
    path('myapp/delete', myapp.views.delete, name="delete"),


]

from . import views
from django.urls import  path
app_name ='food'  # Namespacing:to avoid naming errors.
urlpatterns = [
    path('',views.index,name='index'),
    path('item/',views.item, name='item'),
    path('<int:item_id>/',views.detail,name='detail'),
] 
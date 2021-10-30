from django.urls import path
from .views import(
    product_detail_view,
    product_create_view,
    product_delete_view,
    dynamic_lookup_view,
    product_list_view,
)

app_name= 'products'
urlpatterns = [
    path('<int:id>/',product_detail_view),
    path('create/',product_create_view),
    path('<int:id>/delete/', product_delete_view),
    path('<int:id>/look/', dynamic_lookup_view),
    path('',product_list_view),

]

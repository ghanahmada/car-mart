from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id  
from main.views import register, login_user, logout_user
from main.views import increment_item, decrement_item, delete_item
from main.views import get_item_json, add_item_ajax, delete_item_ajax, increment_item_ajax, decrement_item_ajax
from main.views import create_product_flutter, show_json_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment/<int:id>/', increment_item, name='increment'),
    path('decrement/<int:id>/', decrement_item, name='decrement'),
    path('delete/<int:id>/', delete_item, name='delete'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('increment-item-ajax/<int:id>/', increment_item_ajax, name='increment_item_ajax'),
    path('decrement-item-ajax/<int:id>/', decrement_item_ajax, name='decrement_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('json-user/', show_json_user, name='show_json_user'),
]
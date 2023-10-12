from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_item_amount, reduce_item_amount, delete_item
from main.views import edit_item, delete_item, get_item_json, add_item_ajax, delete_item_ajax

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
    path('add_item_amount/<int:id>/', add_item_amount, name='add_item_amount'),
    path('reduce_item_amount/<int:id>/', reduce_item_amount, name='reduce_item_amount'),
    path('delete_item/', delete_item, name='delete_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete_item_ajax/<int:item_id>/', delete_item_ajax, name='delete_item_ajax'),
]
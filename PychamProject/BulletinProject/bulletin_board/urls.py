from django.urls import path
from . import views

app_name = 'bulletin_board'
urlpatterns = [ #주소 맵핑
    path('', views.index, name='index'),
    path('create/', views.create_bulletin, name='new_bulletin'),
    path('add/', views.add_bulletin, name='insert_bulletin'),
    path('<int:bulletin_id>/', views.view_bulletin, name='view'),
    path('update/<int:bulletin_id>/', views.update_bulletin, name='update'),
    path('delete/<int:bulletin_id>/', views.delete_bulletin, name='delete'),

]
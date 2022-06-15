from django.urls import path
from .views import (
    home, 
    # hello_world, 
    # todoList, 
    # todoCreate, 
    # todoListCreate, 
    # todoUpdate, 
    # todoDelete,
    TodoListCreate,
    # TodoDetail,
)


urlpatterns = [
    path('', home),
    
    #* Function Based Views
    # path('hello/', hello_world),
    # path('todoList/', todoList),
    # path('todoCreate/', todoCreate),
    # path('todoListCreate/', todoListCreate),
    # path('todoUpdate/<int:pk>/', todoUpdate),
    # path('todoDelete/<int:pk>/', todoDelete),
    
    #* Class Based Views
    path("list/", TodoListCreate.as_view()),
    # path("detail/<int:id>", TodoDetail.as_view()),
]
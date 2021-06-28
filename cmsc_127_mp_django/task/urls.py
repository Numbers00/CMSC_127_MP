from django.urls import path, include

from task import views

urlpatterns = [
    path('cards/view/', views.CardsView.as_view()),
    path('boards/view/', views.BoardsView.as_view()),
    path('tasks/view/', views.TasksView.as_view()),
    path('cards/search/', views.card_search),
    path('boards/search/', views.board_search),
    path('tasks/search/', views.task_search),
    path('cards/<slug:card_slug>/', views.CardDetail.as_view()),
    path('boards/<slug:card_slug>/<slug:board_slug>/', views.BoardDetail.as_view()),
    path('tasks/<slug:card_slug>/<slug:board_slug>/<slug:task_slug>/', views.TaskDetail.as_view()),
]
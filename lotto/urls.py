from django.urls import path
from . import views

urlpatterns = [
    path('buy/', views.purchase_lotto, name='purchase_lotto'),
    path('draw/', views.draw_winning_numbers, name='draw_winning_numbers'),  # 이 경로가 정확해야 합니다
    path('check/<int:ticket_id>/', views.check_winning, name='check_winning'),
    path('statistics/', views.lotto_statistics, name='lotto_statistics'),
]

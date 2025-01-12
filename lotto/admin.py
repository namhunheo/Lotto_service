from django.contrib import admin
from .models import LottoTicket, WinningNumbers, Statistics

@admin.register(LottoTicket)
class LottoTicketAdmin(admin.ModelAdmin):
    list_display = ('numbers', 'is_auto', 'created_at')

@admin.register(WinningNumbers)
class WinningNumbersAdmin(admin.ModelAdmin):
    list_display = ('numbers', 'draw_date')

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('draw_date', 'total_tickets', 'total_revenue', 'winning_tickets')

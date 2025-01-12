import re  # re 모듈을 추가해야 합니다.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LottoForm
from .models import LottoTicket, WinningNumbers, Statistics
from django.utils.timezone import now


def purchase_lotto(request):
    """
    로또 티켓 구매 (자동 또는 수동).
    """
    if request.method == "POST":
        form = LottoForm(request.POST)
        if form.is_valid():
            lotto_ticket = form.save(commit=False)
            if lotto_ticket.is_auto:
                lotto_ticket.generate_numbers()
            lotto_ticket.save()
            return render(request, 'lotto/result.html', {'lotto': lotto_ticket})
    else:
        form = LottoForm()
    return render(request, 'lotto/purchase.html', {'form': form})


def draw_winning_numbers(request):
    """
    당첨 번호 추첨 (관리자 전용).
    """
    if request.method == "POST":
        winning_numbers = WinningNumbers()
        winning_numbers.generate_winning_numbers()
        winning_numbers.save()
        return render(request, 'lotto/winning_result.html', {'winning_numbers': winning_numbers})
    return render(request, 'lotto/draw_winning_numbers.html')


def check_winning(request, ticket_id):
    """
    구매한 로또 티켓이 당첨되었는지 확인.
    """
    ticket = get_object_or_404(LottoTicket, id=ticket_id)
    winning_numbers = WinningNumbers.objects.latest('draw_date')  # 최신 당첨 번호
    # 공백과 쉼표를 모두 처리하기 위한 코드
    ticket_numbers = set(map(int, re.split(r'[,\s]+', ticket.numbers)))  # 공백과 콤마를 모두 처리
    drawn_numbers = set(map(int, re.split(r'[,\s]+', winning_numbers.numbers)))  # 공백과 콤마를 모두 처리

    matched_numbers = ticket_numbers & drawn_numbers
    is_winner = len(matched_numbers) == 6  # 모든 번호가 일치하면 당첨

    return render(request, 'lotto/check_result.html', {
        'ticket': ticket,
        'winning_numbers': winning_numbers,
        'matched_numbers': matched_numbers,
        'is_winner': is_winner
    })


def lotto_statistics(request):
    """
    판매 및 당첨 통계 확인 (관리자 전용).
    """
    total_tickets = LottoTicket.objects.count()
    latest_winning_numbers = WinningNumbers.objects.latest('draw_date')
    winning_tickets = LottoTicket.objects.filter(
        numbers__in=latest_winning_numbers.numbers.split(','),
    ).count()

    # 예시: 티켓당 가격 1000원으로 수익 계산
    total_revenue = total_tickets * 1000

    return render(request, 'lotto/statistics.html', {
        'total_tickets': total_tickets,
        'total_revenue': total_revenue,
        'winning_tickets': winning_tickets,
    })

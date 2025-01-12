from django.db import models
import random

class LottoTicket(models.Model):
    """
    LottoTicket 모델은 로또 티켓을 관리합니다.
    - numbers: 생성된 로또 번호 (쉼표로 구분된 문자열)
    - is_auto: 번호 생성 방식 (True: 자동, False: 수동)
    - created_at: 티켓 생성 시간
    """
    numbers = models.CharField(max_length=100)
    is_auto = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_numbers(self):
        """
        번호를 자동으로 생성하는 메서드.
        is_auto가 True일 경우, 1~45 사이에서 6개의 번호를 무작위로 선택.
        """
        if self.is_auto:
            self.numbers = ','.join(map(str, sorted(random.sample(range(1, 46), 6))))


    def __str__(self):
        """
        객체를 문자열로 표현할 때 번호를 표시.
        """
        return f"LottoTicket: {self.numbers} (Auto: {self.is_auto})"


class WinningNumbers(models.Model):
    """
    WinningNumbers 모델은 로또의 당첨 번호를 관리합니다.
    - numbers: 당첨 번호 (쉼표로 구분된 문자열)
    - draw_date: 당첨 번호 추첨 날짜
    """
    numbers = models.CharField(max_length=100)
    draw_date = models.DateTimeField(auto_now_add=True)

    def generate_winning_numbers(self):
        """
        당첨 번호를 무작위로 생성하는 메서드.
        """
        self.numbers = ','.join(map(str, sorted(random.sample(range(1, 46), 6))))
        self.save()

    def __str__(self):
        """
        객체를 문자열로 표현할 때 당첨 번호를 표시.
        """
        return f"Winning Numbers: {self.numbers} (Draw Date: {self.draw_date})"


class Statistics(models.Model):
    """
    Statistics 모델은 로또 판매 및 당첨 통계를 관리합니다.
    - draw_date: 통계 기준 날짜
    - total_tickets: 판매된 전체 티켓 수
    - total_revenue: 총 수익 (예: 티켓 당 가격을 기준으로 계산)
    - winning_tickets: 당첨된 티켓 수
    """
    draw_date = models.DateTimeField()
    total_tickets = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    winning_tickets = models.IntegerField(default=0)

    def __str__(self):
        """
        객체를 문자열로 표현할 때 통계를 표시.
        """
        return (f"Statistics for {self.draw_date}: "
                f"Total Tickets = {self.total_tickets}, "
                f"Total Revenue = {self.total_revenue}, "
                f"Winning Tickets = {self.winning_tickets}")

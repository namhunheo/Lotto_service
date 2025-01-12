# Generated by Django 4.0 on 2025-01-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LottoTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=100)),
                ('is_auto', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.DateTimeField()),
                ('total_tickets', models.IntegerField(default=0)),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('winning_tickets', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WinningNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=100)),
                ('draw_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Lotto',
        ),
    ]
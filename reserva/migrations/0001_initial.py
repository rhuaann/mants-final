# Generated by Django 4.2.7 on 2023-11-23 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instrumento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('pendente', 'Pendente'), ('aprovado', 'Aprovado'), ('negado', 'Negado')], default='pendente', max_length=20, null=True)),
                ('instrumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instrumento.instrumento')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

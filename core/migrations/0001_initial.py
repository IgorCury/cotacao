# Generated by Django 5.0.3 on 2024-03-19 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dadosEmpr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpjReme', models.CharField(max_length=100)),
                ('nomeEprOne', models.CharField(max_length=100)),
                ('telOne', models.CharField(max_length=100)),
                ('logOne', models.CharField(max_length=100)),
                ('ruaOne', models.CharField(max_length=100)),
                ('cityOne', models.CharField(max_length=100)),
                ('estateOne', models.CharField(max_length=100)),
                ('cepOne', models.CharField(max_length=100)),
                ('contaOne', models.CharField(max_length=100)),
                ('cnpjDest', models.CharField(max_length=100)),
                ('nomeEprTwo', models.CharField(max_length=100)),
                ('telTwo', models.CharField(max_length=100)),
                ('logTwo', models.CharField(max_length=100)),
                ('ruaTwo', models.CharField(max_length=100)),
                ('cityTwo', models.CharField(max_length=100)),
                ('estateTwo', models.CharField(max_length=100)),
                ('cepTwo', models.CharField(max_length=100)),
                ('contaTwo', models.CharField(max_length=100)),
                ('nuCOT', models.CharField(max_length=100)),
                ('num1', models.CharField(max_length=100)),
                ('num2', models.CharField(max_length=100)),
                ('num3', models.CharField(max_length=100)),
                ('num4', models.CharField(max_length=100)),
                ('num5', models.CharField(max_length=100)),
                ('num6', models.CharField(max_length=100)),
                ('num7', models.CharField(max_length=100)),
                ('num8', models.CharField(max_length=100)),
                ('num9', models.CharField(max_length=100)),
            ],
        ),
    ]
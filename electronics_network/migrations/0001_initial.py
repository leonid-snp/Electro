# Generated by Django 4.2 on 2024-09-24 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Введите e-mail', max_length=150, unique=True, verbose_name='E-mail')),
                ('country', models.CharField(blank=True, help_text='Введите страну', max_length=60, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, help_text='Введите город', max_length=60, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, help_text='Введите улицу', max_length=60, null=True, verbose_name='Улица')),
                ('house', models.PositiveIntegerField(blank=True, help_text='Введите номер дома', null=True, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='DataMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=60, verbose_name='Название')),
                ('dept', models.PositiveIntegerField(blank=True, help_text='Введите задолженность перед поставщиком', null=True, verbose_name='Задолженность')),
                ('creation_time', models.DateTimeField(blank=True, help_text='Введите время создания', null=True, verbose_name='Время')),
                ('contacts', models.OneToOneField(help_text='Введите контакты', on_delete=django.db.models.deletion.CASCADE, to='electronics_network.contact', verbose_name='Контакты')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=60, verbose_name='Название')),
                ('model', models.CharField(blank=True, help_text='Введите модель', max_length=60, null=True, verbose_name='Модель')),
                ('release', models.DateField(blank=True, help_text='Введите дату выхода на рынок', null=True, verbose_name='Дата выхода')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Entrepreneur',
            fields=[
                ('datamixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronics_network.datamixin')),
            ],
            options={
                'verbose_name': 'Предприниматель',
                'verbose_name_plural': 'Предприниматели',
            },
            bases=('electronics_network.datamixin',),
        ),
        migrations.AddField(
            model_name='datamixin',
            name='products',
            field=models.ManyToManyField(help_text='Введите продукты', to='electronics_network.product', verbose_name='Продукты'),
        ),
        migrations.CreateModel(
            name='RetailChain',
            fields=[
                ('datamixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronics_network.datamixin')),
                ('supplier', models.ForeignKey(blank=True, help_text='Введите поставщика', null=True, on_delete=django.db.models.deletion.SET_NULL, to='electronics_network.entrepreneur', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Розничная сеть',
                'verbose_name_plural': 'Розничные сети',
            },
            bases=('electronics_network.datamixin',),
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('datamixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronics_network.datamixin')),
                ('supplier', models.ForeignKey(blank=True, help_text='Введите поставщика', null=True, on_delete=django.db.models.deletion.SET_NULL, to='electronics_network.retailchain', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Завод',
                'verbose_name_plural': 'Заводы',
            },
            bases=('electronics_network.datamixin',),
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='supplier',
            field=models.ForeignKey(blank=True, help_text='Введите поставщика', null=True, on_delete=django.db.models.deletion.SET_NULL, to='electronics_network.retailchain', verbose_name='Поставщик'),
        ),
    ]

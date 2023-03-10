# Generated by Django 4.1.7 on 2023-03-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modani_app', '0002_alter_sub_category_catolog'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.IntegerField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('product', models.ManyToManyField(to='modani_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('product', models.ManyToManyField(to='modani_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ManyToManyField(to='modani_app.product')),
            ],
        ),
    ]

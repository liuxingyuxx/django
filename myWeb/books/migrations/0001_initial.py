# Generated by Django 2.0.4 on 2018-05-21 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, verbose_name='姓名')),
                ('sex', models.BooleanField(choices=[(0, '男'), (1, '女')], default=0, max_length=1)),
                ('valuation', models.CharField(blank=True, max_length=400, verbose_name='评价')),
                ('book_num', models.IntegerField(blank=True, verbose_name='小说数量')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生日期')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='书名')),
                ('description', models.CharField(max_length=300, verbose_name='简介')),
                ('book_lever', models.DecimalField(decimal_places=1, default=0, help_text='最大值为9.9', max_digits=2, verbose_name='等级')),
                ('book_url', models.URLField(blank=True, max_length=100, verbose_name='链接')),
                ('book_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
            ],
            options={
                'ordering': ('-book_lever',),
                'verbose_name_plural': '书籍',
                'verbose_name': '书籍',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('sex', models.BooleanField(choices=[(0, '男'), (1, '女')], default=0, max_length=1)),
                ('valuation', models.CharField(blank=True, max_length=400, verbose_name='评价')),
                ('power', models.IntegerField(blank=None, help_text='最多为100', verbose_name='战斗力')),
                ('intelligence', models.IntegerField(blank=None, help_text='最多为100', verbose_name='智力')),
                ('ref_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='相关作者', to='books.Author')),
                ('ref_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='相关书', to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
    ]

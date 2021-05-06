# Generated by Django 3.1 on 2020-11-11 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('is_used', models.CharField(choices=[('Y', '사용'), ('N', '사용안함')], default='Y', max_length=1)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.settings')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='videos/')),
                ('is_used', models.CharField(choices=[('Y', '사용'), ('N', '사용안함')], default='Y', max_length=1)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.settings')),
            ],
        ),
        migrations.CreateModel(
            name='QuizChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
                ('is_correct', models.CharField(choices=[('Y', '정답'), ('N', '오답')], default='Y', max_length=1)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commercial.quiz')),
            ],
        ),
    ]
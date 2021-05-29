# Generated by Django 3.1.7 on 2021-05-24 15:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('commercial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RewardCap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_at', models.DateField(default=django.utils.timezone.now)),
                ('daily_cap', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TransactionVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rewarded', models.IntegerField()),
                ('date_at', models.DateField(default=django.utils.timezone.now)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.info')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='commercial.video')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rewarded', models.IntegerField()),
                ('date_at', models.DateField(default=django.utils.timezone.now)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.info')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='commercial.quiz')),
                ('user_choice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='commercial.quizchoices')),
            ],
        ),
    ]

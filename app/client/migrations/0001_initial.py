# Generated by Django 3.1.7 on 2021-05-24 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.CharField(choices=[('B', '법인'), ('I', '개인')], default='B', max_length=1)),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('business_name', models.CharField(max_length=100, null=True)),
                ('business_number', models.CharField(max_length=50, null=True)),
                ('registration_status', models.CharField(choices=[('A', 'APPROVED'), ('P', 'PENDING'), ('D', 'DENIED'), ('U', 'UNREGISTERED')], default='P', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_size', models.IntegerField(default=1000)),
                ('exposed_size', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('payment_status', models.CharField(choices=[('P', 'PENDING'), ('R', 'REQUESTING'), ('D', 'DENIED'), ('A', 'APPROVED'), ('C', 'COMPLETED')], default='P', max_length=1)),
                ('register_at', models.DateField(default=django.utils.timezone.now)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.info')),
            ],
        ),
        migrations.CreateModel(
            name='TargetLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('L0', '상관없음'), ('L1', '서울'), ('L2', '경기'), ('L3', '강원'), ('L4', '충청'), ('L5', '경상'), ('L6', '전라'), ('L7', '제주')], default='L0', max_length=2)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.settings')),
            ],
        ),
        migrations.CreateModel(
            name='TargetInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(choices=[('NO', '없음'), ('SP', '스포츠'), ('GA', '게임'), ('MU', '음악'), ('MO', '영화'), ('TR', '여행'), ('FO', '음식'), ('SI', '자기개발'), ('DA', '춤'), ('TE', '기술'), ('AN', '동물')], default='NO', max_length=2)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.settings')),
            ],
        ),
        migrations.CreateModel(
            name='TargetGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('G0', '상관없음'), ('GM', '남'), ('GF', '여')], default='G0', max_length=2)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.settings')),
            ],
        ),
        migrations.CreateModel(
            name='TargetAge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(choices=[('A0', '상관없음'), ('A1', '0~19'), ('A2', '20~29'), ('A3', '30~39'), ('A4', '40~49'), ('A5', '50~59'), ('A6', '60+')], default='A0', max_length=2)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.settings')),
            ],
        ),
    ]

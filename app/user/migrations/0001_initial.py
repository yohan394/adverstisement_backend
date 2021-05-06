# Generated by Django 3.1 on 2020-11-17 04:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_status', models.CharField(choices=[('A', 'ACTIVE'), ('I', 'INACTIVE')], default='A', max_length=1)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('bank_type', models.CharField(max_length=30, null=True)),
                ('account_number', models.CharField(max_length=70, null=True)),
                ('age', models.IntegerField(max_length=3, null=True)),
                ('reg_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_ip', models.CharField(max_length=50)),
                ('last_login_dt', models.DateField(default=django.utils.timezone.now)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.info')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('L0', '상관없음'), ('L1', '서울'), ('L2', '경기'), ('L3', '강원'), ('L4', '충청'), ('L5', '경상'), ('L6', '전라'), ('L7', '제주')], default='L0', max_length=2)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.info')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(choices=[('NO', '없음'), ('SP', '스포츠'), ('GA', '게임'), ('MU', '음악'), ('MO', '영화'), ('TR', '여행'), ('FO', '음식'), ('SI', '자기개발'), ('DA', '춤'), ('TE', '기술'), ('AN', '동물')], default='NO', max_length=2)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.info')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('G0', '상관없음'), ('GM', '남'), ('GF', '여')], default='G0', max_length=2)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.info')),
            ],
        ),
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.CharField(choices=[('A0', '상관없음'), ('A1', '0~19'), ('A2', '20~29'), ('A3', '30~39'), ('A4', '40~49'), ('A5', '50~59'), ('A6', '60+')], default='A0', max_length=2)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.info')),
            ],
        ),
    ]
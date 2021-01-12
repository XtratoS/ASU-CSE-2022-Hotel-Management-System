# Generated by Django 3.1.4 on 2021-01-12 07:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthDay', models.DateField(default=None, null=True, verbose_name='Birthday')),
                ('phoneNumber', models.PositiveBigIntegerField(default=0)),
                ('account_type', models.CharField(max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='schedule day')),
                ('start_time', models.TimeField(default=datetime.time(8, 0), verbose_name='')),
                ('end_time', models.TimeField(default=datetime.time(2, 0), verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.person')),
                ('height', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
            ],
            bases=('system.person',),
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.person')),
                ('salary', models.IntegerField(default=0)),
                ('schedule', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.schedule')),
            ],
            bases=('system.person',),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_price', models.IntegerField(default=0)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_taken', models.BooleanField(default=False)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('staffmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.staffmember')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.department')),
                ('patients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.patient')),
            ],
            bases=('system.staffmember',),
        ),
        migrations.CreateModel(
            name='EmergencyEmployee',
            fields=[
                ('staffmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.staffmember')),
            ],
            bases=('system.staffmember',),
        ),
        migrations.CreateModel(
            name='FinanceEmployee',
            fields=[
                ('staffmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.staffmember')),
            ],
            bases=('system.staffmember',),
        ),
        migrations.CreateModel(
            name='FrontdeskEmployee',
            fields=[
                ('staffmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.staffmember')),
            ],
            bases=('system.staffmember',),
        ),
        migrations.CreateModel(
            name='HospitalManager',
            fields=[
                ('staffmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.staffmember')),
            ],
            bases=('system.staffmember',),
        ),
        migrations.CreateModel(
            name='LabSpecialist',
            fields=[
                ('staffmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.staffmember')),
            ],
            bases=('system.staffmember',),
        ),
        migrations.CreateModel(
            name='RadiologySpecialist',
            fields=[
                ('staffmember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.staffmember')),
            ],
            bases=('system.staffmember',),
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_describtion', models.TextField(max_length=1000)),
                ('medical_problems', models.TextField(max_length=1000)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None, verbose_name='Appointment Date')),
                ('startTime', models.TimeField(default=datetime.time(8, 0), verbose_name='start time')),
                ('is_booked', models.BooleanField(default=False)),
                ('is_payed', models.BooleanField(default=False)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='system.schedule')),
                ('service', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.service')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.patient')),
            ],
            options={
                'ordering': ['startTime'],
            },
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_manager',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.hospitalmanager'),
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=1000)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.doctor')),
            ],
        ),
    ]

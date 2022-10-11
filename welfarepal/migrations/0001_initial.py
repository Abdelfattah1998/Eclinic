# Generated by Django 2.2.4 on 2022-10-11 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=45)),
                ('Last_Name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('Certificate', models.CharField(max_length=45)),
                ('Location', models.CharField(max_length=45)),
                ('Specialization', models.CharField(max_length=45)),
                ('Experience', models.DateTimeField()),
                ('Phone_Number', models.IntegerField()),
                ('MedicalNumber', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=45)),
                ('Last_Name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('Personal_ID', models.CharField(max_length=45)),
                ('Marital_Status', models.CharField(max_length=45)),
                ('Gender', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagnosis', models.CharField(max_length=45)),
                ('Medicines', models.CharField(max_length=45)),
                ('Description', models.CharField(max_length=45)),
                ('Examinations', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='welfarepal.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='welfarepal.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancies', models.DateTimeField()),
                ('clinic', models.CharField(max_length=45)),
                ('clinic_phone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='welfarepal.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='welfarepal.Patient')),
            ],
        ),
    ]
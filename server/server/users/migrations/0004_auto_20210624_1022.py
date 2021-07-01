# Generated by Django 3.1.11 on 2021-06-24 07:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210608_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
            ],
            options={
                'verbose_name_plural': '4. Instructor (Guide)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('CONSUMER', 'Consumer'), ('COORDINATOR', 'Coordinator'), ('VENDOR', 'Vendor'), ('INSTRUCTOR', 'Instructor')], default='CONSUMER', max_length=50, verbose_name='Type'),
        ),
        migrations.CreateModel(
            name='InstructorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=50, verbose_name='Gender')),
                ('profile_picture', models.JSONField(blank=True, default=dict, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='phone number must be between 9-15 digits', regex='^\\d{9,15}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructorprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
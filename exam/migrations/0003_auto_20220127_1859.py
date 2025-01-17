# Generated by Django 3.2.8 on 2022-01-27 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0002_exam_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('info', models.TextField()),
                ('duration', models.DurationField(help_text='hr:min:sec = 00:00:00')),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam_detail')),
            ],
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=15)),
                ('option2', models.CharField(max_length=15)),
                ('option3', models.CharField(max_length=15)),
                ('option4', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=15)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exam.exam_detail')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exam.mcq')),
            ],
        ),
        migrations.RemoveField(
            model_name='exam',
            name='examiner',
        ),
        migrations.RemoveField(
            model_name='option',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='test',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='test',
            name='examinee',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-14 15:38

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
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('video', models.CharField(max_length=200)),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lockedinapi.difficulty')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lockedinapi.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lockedinapi.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('exerciseRoutine', models.ManyToManyField(through='lockedinapi.ExerciseRoutine', to='lockedinapi.routine')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentWeight', models.IntegerField()),
                ('goalWeight', models.IntegerField()),
                ('timeframe', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exerciseroutine',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lockedinapi.routine'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscleGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lockedinapi.musclegroup'),
        ),
    ]

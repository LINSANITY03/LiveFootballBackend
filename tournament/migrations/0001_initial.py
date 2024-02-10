# Generated by Django 4.1.7 on 2024-02-10 10:23

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo_img', models.ImageField(blank=True, null=True, upload_to='photos/tournament')),
                ('total_games', models.IntegerField(default=0)),
                ('total_teams', models.IntegerField(choices=[(2, '2'), (4, '4'), (8, '8')], default=2)),
                ('time_games', models.IntegerField(choices=[(5, '5'), (10, '10'), (20, '20')], default=5)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'db_table': 'Tournament',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo_img', models.ImageField(blank=True, null=True, upload_to='photos/teams')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tourn_team', to='tournament.tournament')),
            ],
            options={
                'db_table': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo_img', models.ImageField(blank=True, null=True, upload_to='photos/<django.db.models.fields.related.ForeignKey>')),
                ('jersey_no', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='team_player', to='tournament.teams')),
            ],
            options={
                'db_table': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.IntegerField(choices=[(0, 'TBD'), (1, 'Ongoing'), (2, 'Completed')], default=0)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='awayteam', to='tournament.teams')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hometeam', to='tournament.teams')),
            ],
            options={
                'db_table': 'GamesHistory',
            },
        ),
    ]

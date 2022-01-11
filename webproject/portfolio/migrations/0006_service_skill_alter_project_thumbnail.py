# Generated by Django 4.0 on 2021-12-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('skill_icon', models.ImageField(blank=True, default='about-img.png', null=True, upload_to='image/skill-icon')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/gallery/gallery-1.jpg', null=True, upload_to='images'),
        ),
    ]
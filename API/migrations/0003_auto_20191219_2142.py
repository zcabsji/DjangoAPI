# Generated by Django 3.0 on 2019-12-19 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20191219_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='uid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='QuestionnairesList', to='API.User'),
        ),
    ]
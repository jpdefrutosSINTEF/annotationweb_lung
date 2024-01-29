# Generated by Django 2.2.13 on 2023-11-24 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('annotationweb', '0006_auto_20231124_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLabelBlind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='annotationweb.KeyFrameAnnotation')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotationweb.Label')),
            ],
        ),
    ]

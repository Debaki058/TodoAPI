5

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=100)),
                ('age', models.BigIntegerField()),
                ('mobile_number', models.BigIntegerField()),
                ('roll_number', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]



from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_student_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_comment_options_alter_post_options"),
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE blog_comment DROP COLUMN challenge",
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]

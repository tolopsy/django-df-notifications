# Generated by Django 4.1.6 on 2023-02-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_notifications', '0002_remove_notificationhistory_df_notifica_templat_fc63aa_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='notificationhistory',
            name='df_notifica_templat_ec4b48_idx',
        ),
        migrations.RenameField(
            model_name='notificationhistory',
            old_name='template',
            new_name='template_prefix',
        ),
        migrations.AddIndex(
            model_name='notificationhistory',
            index=models.Index(fields=['template_prefix', 'created'], name='df_notifica_templat_fc63aa_idx'),
        ),
    ]

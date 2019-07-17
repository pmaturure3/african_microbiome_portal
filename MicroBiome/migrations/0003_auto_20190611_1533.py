# Generated by Django 2.2.2 on 2019-06-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MicroBiome', '0002_auto_20190418_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='amplicon_target',
        ),
        migrations.RemoveField(
            model_name='project',
            name='antibiotic_regimen',
        ),
        migrations.RemoveField(
            model_name='project',
            name='avg_spotlen',
        ),
        migrations.RemoveField(
            model_name='project',
            name='bioproject',
        ),
        migrations.RemoveField(
            model_name='project',
            name='bioproject_links',
        ),
        migrations.RemoveField(
            model_name='project',
            name='bioproject_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='biosample',
        ),
        migrations.RemoveField(
            model_name='project',
            name='biosample_model',
        ),
        migrations.RemoveField(
            model_name='project',
            name='birth_delivery',
        ),
        migrations.RemoveField(
            model_name='project',
            name='bp_count',
        ),
        migrations.RemoveField(
            model_name='project',
            name='case_control',
        ),
        migrations.RemoveField(
            model_name='project',
            name='centre_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='collection_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='consent',
        ),
        migrations.RemoveField(
            model_name='project',
            name='coordinate',
        ),
        migrations.RemoveField(
            model_name='project',
            name='datastore_provider',
        ),
        migrations.RemoveField(
            model_name='project',
            name='disease_stage',
        ),
        migrations.RemoveField(
            model_name='project',
            name='ena_last_update',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_biome',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_feature',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_material',
        ),
        migrations.RemoveField(
            model_name='project',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='project',
            name='fastq_ftp',
        ),
        migrations.RemoveField(
            model_name='project',
            name='host',
        ),
        migrations.RemoveField(
            model_name='project',
            name='host_body_mass_index',
        ),
        migrations.RemoveField(
            model_name='project',
            name='host_taxa_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='insert_size',
        ),
        migrations.RemoveField(
            model_name='project',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='project',
            name='isolation_source',
        ),
        migrations.RemoveField(
            model_name='project',
            name='lat_ion',
        ),
        migrations.RemoveField(
            model_name='project',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='project',
            name='library_layout',
        ),
        migrations.RemoveField(
            model_name='project',
            name='library_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='library_source',
        ),
        migrations.RemoveField(
            model_name='project',
            name='libraryselection',
        ),
        migrations.RemoveField(
            model_name='project',
            name='load_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='project',
            name='mbases',
        ),
        migrations.RemoveField(
            model_name='project',
            name='mbytes',
        ),
        migrations.RemoveField(
            model_name='project',
            name='mg_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='mg_rast_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='organism',
        ),
        migrations.RemoveField(
            model_name='project',
            name='physical_specimen_remaining',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pmid',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pregnant',
        ),
        migrations.RemoveField(
            model_name='project',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='repository',
        ),
        migrations.RemoveField(
            model_name='project',
            name='run',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sample_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='seq_count',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='project',
            name='special_diet',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sra_sample',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sra_study',
        ),
        migrations.AddField(
            model_name='project',
            name='disease',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='lon',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='repo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='repository_id',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='sample_count',
            field=models.PositiveSmallIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='sample_type',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='study_design',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='study_link',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='assay_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='country',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='platform',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='study_title',
            field=models.CharField(default=False, max_length=280),
        ),
    ]

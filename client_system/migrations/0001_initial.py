# Generated by Django 4.1 on 2023-01-06 06:36

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
            name='ClientDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Client Name')),
                ('sex', models.CharField(max_length=200, verbose_name='Sex')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Telephone Number')),
                ('id_no', models.IntegerField(verbose_name='ID/Passport No')),
                ('sub_county', models.CharField(max_length=200, verbose_name='Client Name')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Devorced', 'Divorced'), ('Separated', 'Separated'), ('Other', 'Other')], max_length=200, verbose_name='Marital Status')),
                ('occupation', models.CharField(max_length=200, verbose_name='Occupation')),
                ('income', models.CharField(choices=[('0', '0'), ('<6000KES', '<6000KES'), ('6000-15000kES', '6000-15000KSH'), ('15,000-25,000KSH', '15000-25000kSH'), ('>25000KSH', '>250000KSH')], max_length=200, verbose_name='Income Per Month')),
                ('education', models.CharField(max_length=200, verbose_name='Educational Attainement')),
                ('ref_institution', models.CharField(max_length=200, verbose_name='Reffering Instituition')),
                ('refferal_date', models.DateField(blank=True, max_length=200, null=True, verbose_name='Date Reffered')),
                ('contact_person', models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact Person')),
                ('kin_name', models.CharField(max_length=200, verbose_name='Name of Next Of Kin')),
                ('kin_address', models.CharField(max_length=200, verbose_name='Address of Next Of Kin')),
                ('kin_residence', models.CharField(max_length=200, verbose_name='Residence of Next Of Kin')),
                ('kin_occupation', models.CharField(max_length=200, verbose_name='Occupation of Next Of Kin')),
                ('hiv_status', models.CharField(choices=[('Positive', 'Positve'), ('Negative', 'Negative')], max_length=200, verbose_name='HIV Status')),
                ('madical', models.CharField(blank=True, max_length=200, null=True, verbose_name='Madical Condition if Any')),
                ('hiv_involve', models.TextField(blank=True, null=True, verbose_name='HIV Issue Involved')),
                ('case_type', models.CharField(choices=[('Boundary Dispute', 'Boundary Dispute'), ('Eviction', 'Eviction'), ('Succesion/Inheritaance', 'Succesion/Inheritaance'), ('Divison Of Martrimonial Property', 'Divison Of Martrimonial Property'), ('Custody/Maintenance', 'Custody/Maintenance'), ('Land Title Acquisition', 'Land Title Acquisition'), ('Employment Denial/Dismissal', 'Employment Denial/Dismissal'), ('Burial Dispute', 'Burial Dispute'), ('Defilement', 'Defilement'), ('Rape', 'Rape'), ('FGM', 'FGM'), ('Sterilization', 'Sterilazation'), ('Access To Medicine', 'Access To MEdicine'), ('Wrongful Diagnosis', 'Wrongfull Diagnosis'), ('Forced Hospitalizaton', 'Forced Hospitalization'), ('Other', 'Other')], max_length=200, verbose_name='Type of the Case')),
                ('case_detail', models.TextField(verbose_name='Detail of the case')),
                ('adr_detail', models.TextField(blank=True, null=True, verbose_name='Give ADR Details')),
                ('court_detail', models.TextField(blank=True, null=True, verbose_name='Give Court Details')),
                ('outcome', models.TextField(blank=True, null=True, verbose_name='Give Court Outcome')),
                ('documents', models.FileField(upload_to='cases', verbose_name='Uploads all supporting documnets')),
                ('action_taken', models.CharField(choices=[('Probon Laywer', 'Probono Lawyer'), ('Police', 'Police'), ('Other NGO', 'Other NGO'), ('Govt Dept', 'Goverment Department'), ('Take Up Case', 'Take Up Case'), ('Self Representation', 'Self Representation'), ('Only Legal advice', 'Only Legal advice'), ('Not a  case', 'Not a case')], max_length=200, verbose_name='Action Taken')),
                ('action_detail', models.TextField(verbose_name='Give Details')),
                ('about_kelin', models.CharField(choices=[('Radio', 'Radio'), ('Television', 'Telwvision'), ('Print Media', 'Print Media'), ('Church', 'Church'), ('Relative', 'Relative'), ('Referall(form)', 'Refferal(form)'), ('Social Media', 'Socila Media'), ('Training/Forum', 'Training/Forum'), ('CBO', 'CBO'), ('Elders', 'Elders'), ('Internet', 'Internet'), ('Friend/Famil', 'Friend/Family'), ('Other', 'Other')], max_length=200, verbose_name='About Kelin')),
                ('cepa', models.CharField(max_length=200, verbose_name='CEPA material Issued')),
                ('committment', models.FileField(upload_to='commitments', verbose_name='Commitment')),
            ],
        ),
        migrations.CreateModel(
            name='CleintEngament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Client Name')),
                ('county', models.CharField(max_length=200, verbose_name='County')),
                ('subcounty', models.CharField(max_length=200, verbose_name='Subcounty')),
                ('number', models.CharField(max_length=200, verbose_name='Contact Number')),
                ('notes', models.TextField()),
                ('officer_comment', models.TextField()),
                ('reffer_to', models.CharField(max_length=200, verbose_name='Reffer To')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

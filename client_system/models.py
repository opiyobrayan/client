from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CleintEngament(models.Model):
    name=models.CharField('Client Name',max_length=200)
    county=models.CharField('County',max_length=200)
    subcounty=models.CharField('Subcounty',max_length=200)
    number=models.CharField('Contact Number',max_length=200)
    officer=models.ForeignKey(User,on_delete=models.CASCADE)
    notes=models.TextField()
    officer_comment=models.TextField()
    reffer_to=models.CharField('Reffer To',max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# client detail form


MARITAL_CHOICES= [
    ('single', 'Single'),
    ('Married', 'Married'),
    ('Widowed', 'Widowed'),
    ('Devorced', 'Divorced'),
    ('Separated', 'Separated'),
    ('Other', 'Other'),
    ]
CLIENT_INCOME=[
    ('0', '0'),
    ('<6000KES', '<6000KES'),
    ('6000-15000kES', '6000-15000KSH'),
    ('15,000-25,000KSH', '15000-25000kSH'),
    ('>25000KSH', '>250000KSH'),
   

]
HIV_STATUS=[
    ('Positive','Positve'),
    ('Negative','Negative')
]
CASE_TYPE=[
    ('Boundary Dispute','Boundary Dispute'),
    ('Eviction','Eviction'),
    ('Succesion/Inheritaance','Succesion/Inheritaance'),
    ('Divison Of Martrimonial Property','Divison Of Martrimonial Property'),
    ('Custody/Maintenance','Custody/Maintenance'),
    ('Land Title Acquisition','Land Title Acquisition'),
    ('Employment Denial/Dismissal','Employment Denial/Dismissal'),
    ('Burial Dispute','Burial Dispute'),
    ('Defilement','Defilement'),
    ('Rape','Rape'),
    ('FGM','FGM'),
    ('Sterilization','Sterilazation'),
    ('Access To Medicine','Access To MEdicine'),
    ('Wrongful Diagnosis','Wrongfull Diagnosis'),
    ('Forced Hospitalizaton','Forced Hospitalization'),
    ('Other','Other'),
]
ACTION_TAKEN=[
    ('Probon Laywer','Probono Lawyer'),
    ('Police','Police'),
    ('Other NGO','Other NGO'),
    ('Govt Dept','Goverment Department'),
    ('Take Up Case','Take Up Case'),
    ('Self Representation','Self Representation'),
    ('Only Legal advice','Only Legal advice'),
    ('Not a  case','Not a case'),

]
KELIN_HEAR=[
    ('Radio','Radio'),
    ('Television','Telwvision'),
    ('Print Media','Print Media'),
    ('Church','Church'),
    ('Relative','Relative'),
    ('Referall(form)','Refferal(form)'),
    ('Social Media','Socila Media'),
    ('Training/Forum','Training/Forum'),
    ('CBO','CBO'),
    ('Elders','Elders'),
    ('Internet','Internet'),
    ('Friend/Famil','Friend/Family'),
    ('Other','Other'),
    
]


class ClientDetail(models.Model):
    
    # client ddeatails
    name=models.CharField('Client Name',max_length=200)
    sex=models.CharField('Sex',max_length=200)
    age=models.IntegerField('Age',blank=True,null=True)
    phone=models.IntegerField('Telephone Number',blank=True,null=True)
    id_no=models.IntegerField('ID/Passport No')
    sub_county=models.CharField('Client Name',max_length=200)
    address=models.CharField('Address',max_length=200)
    marital_status=models.CharField('Marital Status',choices=MARITAL_CHOICES,max_length=200)
    occupation=models.CharField('Occupation',max_length=200)
    income=models.CharField('Income Per Month',choices=CLIENT_INCOME,max_length=200)
    education=models.CharField('Educational Attainement',max_length=200)
    ref_institution=models.CharField('Reffering Instituition',max_length=200)
    refferal_date=models.DateField('Date Reffered',max_length=200,null=True,blank=True)
    contact_person=models.CharField('Contact Person',max_length=200,null=True,blank=True)
    

    # next of kin detals
    kin_name=models.CharField('Name of Next Of Kin',max_length=200)
    kin_address=models.CharField('Address of Next Of Kin',max_length=200)
    kin_residence=models.CharField('Residence of Next Of Kin',max_length=200)
    kin_occupation=models.CharField('Occupation of Next Of Kin',max_length=200)

    # hiv status
    hiv_status=models.CharField('HIV Status',choices=HIV_STATUS,max_length=200)
    madical=models.CharField('Madical Condition if Any',max_length=200,null=True,blank=True)
    hiv_involve=models.TextField('HIV Issue Involved',null=True,blank=True)

    # Details of the case
    case_type=models.CharField('Type of the Case',choices=CASE_TYPE,max_length=200)
    case_detail=models.TextField('Detail of the case')

    # ADR
    adr_detail=models.TextField('Give ADR Details',null=True,blank=True)

    # Court attendance

    court_detail=models.TextField('Give Court Details',null=True,blank=True)
    outcome=models.TextField('Give Court Outcome',null=True,blank=True)
    
    # documentation

    documents=models.FileField('Uploads all supporting documnets',upload_to='cases')

    # action taken

    action_taken=models.CharField('Action Taken',choices=ACTION_TAKEN,max_length=200)
    action_detail=models.TextField('Give Details')

    # How did you hear about KELIN

    about_kelin=models.CharField('About Kelin',choices=KELIN_HEAR,max_length=200)

    #CEPA material issued

    cepa=models.CharField('CEPA material Issued',max_length=200)

    # comments

    committment=models.FileField('Commitment',upload_to='commitments')

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User





# Create your models here.
JOB_TYPE = (
    ('Full-time', 'Full-time'), ('Part-time','Part-time'), ('Contract','Contract'), ('Internship','Internship')
)

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class jobListing(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(choices=JOB_TYPE, max_length=20)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30,blank=True)
    company_name = models.CharField(max_length=300)
    company_description = models.TextField(blank=True, null=True)
    requirements = models.TextField()
    url = models.URLField(max_length=200)    
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    special_instructions = models.TextField(blank=True, null=True)
    logo_image = models.ImageField(upload_to='logos')
    

    def __str__(self):
        return self.title
class save_job(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(jobListing,on_delete=models.CASCADE)
    saved_time = models.DateTimeField(auto_now=True)

class jobapplication(models.Model):
    job = models.ForeignKey(jobListing,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='applicant_resumes/')
    applied_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.job.title} {self.name}'

class Userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    email = models.EmailField()
    birthdate = models.DateField()
    bio = models.TextField(blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=False)
    ssc_percentage = models.FloatField(blank=False)
    hsc_percentage = models.FloatField(blank=False)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_year = models.IntegerField(null=True,blank=True)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/',blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



     


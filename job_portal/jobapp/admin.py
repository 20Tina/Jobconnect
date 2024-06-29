from django.contrib import admin
from .models import jobListing,Category,save_job,jobapplication,Userprofile 
# Register your models here.
admin.site.register(Category)
@admin.register(jobListing)
class jobListingAdmin(admin.ModelAdmin):
    list_display=['title','company_name','company_description','requirements','location','job_type','salary','category']

@admin.register(save_job)
class save_jobAdmin(admin.ModelAdmin):
    list_display=['user','job','saved_time']

@admin.register(jobapplication)
class jobapplication(admin.ModelAdmin):
    list_display=['job','name','email','phone_number','cover_letter','resume','applied_date']

@admin.register(Userprofile)
class Userprofile(admin.ModelAdmin):
    list_display=['user','profile_picture','email','birthdate','bio','phone_number','ssc_percentage','hsc_percentage','degree','institution','graduation_year','skills','resume']

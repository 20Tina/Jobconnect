from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .models import jobListing,save_job,jobapplication,Category,Userprofile







# Create your views here.
def index(request):
    recent_listings=jobListing.objects.all()[:3]
    search_results = None
    data=jobListing.objects.all()[:2]

    if 'job_type' in request.GET:
        job_type_query = request.GET['job_type']
        if jobListing.objects.filter(job_type__icontains=job_type_query).exists():
            search_results = {'message': f'The job type "{job_type_query}" is available. Sign in to view jobs.'}
        else:
            search_results = {'message':f'The job type "{job_type_query}" is not available. Sign in to view jobs.'}

   
    return render(request, 'index.html', {'recent_listings': recent_listings, 'search_results': search_results,'joblisting':data})

def register(request):  
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            try:
                user = User.objects.create_user(username=email,first_name=fname,last_name=lname,email=email,password=pass1)
                user.save()
                return redirect('login')
            except:
                error = "User already exists"
                return render(request,'joblisting.html',{'error':error})
        else:
            error = 'password does not match'
            return render(request,'registration.html',{'error':error})
    return render(request,'registration.html')


def user_login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1= request.POST['pass1']
        user = authenticate(username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('joblisting')
        else:
            error = "Invalid username or password"
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')


@never_cache
def joblisting(request):
    job_listings = jobListing.objects.all()
    recent_listings = job_listings.order_by('-id')[:5]
    location = request.GET.get('location','')
    job_type = request.GET.get('job_type')
    title = request.GET.get('title','')
   
   

    if title:
        job_listings = job_listings.filter(title__icontains=title)
    if location:
        job_listings = job_listings.filter(location__icontains=location)
    if job_type:
        job_listings = job_listings.filter(job_type=job_type)
    

            
    context = {
        'job_listings': job_listings,
        'selected_location': location,  
        'selected_job_type': job_type,
        'selected_title':title,
        'recent_listings':recent_listings,
       
       
       
      
        
    }

    
    
     
    return render(request, 'joblisting.html', context)

def view_job(request,jid):
   job=jobListing.objects.get(id=jid)
   first_name=request.user.first_name
   last_name=request.user.last_name
   full_name=f"{first_name} {last_name}"
   email=request.user.email
   applied_jobs = jobapplication.objects.filter(email=request.user.email,job=job).exists

   context = {
        'job': job,
        'full_name': full_name,
        'email': email,
        'already_applied': applied_jobs,
   }
   
    
   return render(request,'view_job.html',context)



def dashboard(request):
    if request.user.is_authenticated:
        saved_jobs = save_job.objects.filter(user=request.user)[:3]
    if request.user.is_authenticated:
        applied_jobs = jobapplication.objects.filter(email=request.user.email)[:3]
    if request.user.is_authenticated:
        user_profile_instance = Userprofile.objects.filter(user=request.user).first()
    return render(request,'dashboard.html',{'saved_jobs':saved_jobs,'applied_jobs':applied_jobs,'user_profile_instance':user_profile_instance})

def postjob(request):
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST.get('title')
        company_description = request.POST.get('company_description')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        job_type = request.POST.get('job_type')
        company_name = request.POST.get('company_name')
        logo_image = request.FILES.get('logo_image')
        requirements = request.POST.get('requirements')
        special_instructions = request.POST.get('special_instructions')
        url = request.POST.get('url')
        last_date = request.POST.get('last_date')
        category_id = request.POST.get('category')
        category = Category.objects.get(pk=category_id)
 
        
        job = jobListing.objects.create(
            title=title,
            company_description=company_description,
            location=location,
            salary=salary,
            job_type=job_type,
            company_name=company_name,
            logo_image=logo_image,
            requirements=requirements,
            special_instructions=special_instructions,
            url=url,
            last_date=last_date,
            category=category
        )
        job.save()
        return redirect('postjob')

    return render(request, 'postjob.html')

def save_application(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    full_name = f"{first_name} {last_name}" 

    
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        if job_id:
            job = jobListing.objects.get(id=job_id)
            save_job.objects.create(user=request.user, job=job)
            return redirect('save_application') 

    
    if request.user.is_authenticated:
        saved_jobs = save_job.objects.filter(user=request.user)
    else:
        return redirect('login')


    user_profile_instance = Userprofile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        resume = request.FILES.get('resume')
        email = request.POST.get('email')
        birthdate = request.POST.get('birthdate')
        bio = request.POST.get('bio')
        phone_number = request.POST.get('phone_number')
        ssc_percentage = request.POST.get('ssc_percentage')
        hsc_percentage = request.POST.get('hsc_percentage')
        degree = request.POST.get('degree')
        institution = request.POST.get('institution')
        graduation_year = request.POST.get('graduation_year')
        skills = request.POST.get('skills')

        if user_profile_instance:
            if profile_picture:
                user_profile_instance.profile_picture = profile_picture
            if resume:
                user_profile_instance.resume = resume  
           
            user_profile_instance.email = email
            user_profile_instance.birthdate = birthdate
            user_profile_instance.bio = bio
            user_profile_instance.phone_number = phone_number
            user_profile_instance.ssc_percentage = ssc_percentage
            user_profile_instance.hsc_percentage = hsc_percentage
            user_profile_instance.degree = degree
            user_profile_instance.institution = institution
            user_profile_instance.graduation_year = graduation_year
            user_profile_instance.skills = skills

            user_profile_instance.save()
        else:
            Userprofile.objects.create(
                user=request.user,
                profile_picture=profile_picture,
                email=email,
                birthdate=birthdate,
                bio=bio,
                phone_number=phone_number,
                ssc_percentage=ssc_percentage,
                hsc_percentage=hsc_percentage,
                degree=degree,
                institution=institution,
                graduation_year=graduation_year,
                skills=skills,
                resume=resume
            )

        return redirect('save_application')
    
    return render(request, 'save_application.html', {'saved_jobs': saved_jobs, 'user_profile_instance': user_profile_instance,'full_name':full_name})

def delete_save_job(request,job_id):
    saved_jobs = save_job.objects.get(id=job_id)
    saved_jobs.delete()
    return redirect('save_application')

def job_applied(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')

        job_application = jobapplication.objects.create(job_id=job_id,name=name,email=email,phone_number=phone_number,cover_letter=cover_letter,resume=resume)
        job_application.save()

        messages.success(request, 'Your application has been submitted successfully!')

        return redirect('job_applied')

    applied_jobs = jobapplication.objects.filter(email=request.user.email)
    return render(request,'job_applied.html',{'applied_jobs':applied_jobs})
        

def del_job_applied(request, job_id):
    try:
        job_application = jobapplication.objects.get(id=job_id)
        job_application.delete()
    except jobapplication.DoesNotExist:
        pass
    return redirect('job_applied')


def about(request):
    return render(request,'about.html')

def user_logout(request):
    logout(request)
    return redirect('index')
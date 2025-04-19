from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from account.models import Organization, UserProfile , CustomUser
from myapp.models import Jobpost,Notification_model
from myapp.form import JobPostForm,JobFilterForm
from django.contrib import messages

@login_required
def Home(request):
    jobs = None
    user = CustomUser.objects.get(email = request.user.email)
    if user.is_organization:
        organization = Organization.objects.get(user = user)
        job_post = Jobpost.objects.filter(organization_name = organization.name)
        if organization:
            required_fields = [organization.name, organization.address, organization.website]
            if not all(required_fields):
                return redirect("edit_profile")
            
        else:
            return redirect("edit_profile")
    else:
        user_profile = UserProfile.objects.get(user = user)
        if user_profile:
            required_fields = [user_profile.address, user_profile.skills,
                               user_profile.country,user_profile.city]
            if not all(required_fields):
                return redirect("edit_profile")
            else:
                jobs = Jobpost.objects.order_by('?')[:20]
                print(jobs)
            
        else:
            return redirect("edit_profile")
        
    job_post = Jobpost.objects.all()
    job_filter_form = JobFilterForm()

    if request.method == 'POST':
        # Check which form was submitted
        if 'search_filter' in request.POST:
            job_filter_form = JobFilterForm(request.POST)
            if job_filter_form.is_valid():
                data = job_filter_form.cleaned_data
                job_post = Jobpost.objects.filter(
                    organization_name=data['organization_name'],
                    job_name=data['job_name'],
                    location=data['location'],
                    location_type=data['location_type'],
                    salary=data['salary'],
                    experience_required=data['experience_required'],
                    job_type=data['job_type'],
                )
                if job_post.exists():
                    messages.success(request, "Jobs filtered successfully.")
                else:
                    messages.error(request, "No matching job found.")
            else:
                messages.error(request, job_filter_form.errors)

        elif 'apply_job' in request.POST:
            try:
                sender = CustomUser.objects.get(email=request.user.email)
                receiver_id = request.POST.get('job_post_owner_id')
                receiver = CustomUser.objects.get(id=receiver_id)
                job_id = request.POST.get('job_post_id')
                job = Jobpost.objects.get(id=job_id)

                job.applied_users.add(sender)
                job.save()

                Notification_model.objects.create(
                    sender=sender,
                    receiver=receiver,
                    job_post=job,
                    message=f"{sender.first_name} {sender.last_name} applied for the job {job.title}",
                    file=sender.resume,
                )

                messages.success(request, "Successfully applied for the job.")
            except Exception as e:
                messages.error(request, f"Failed to apply: {e}")

    return render(request, "Home.html", {
        'job_post': job_post,
        'job_filter_form': job_filter_form
    })
def Job_Post_View(request):
    form = None
    user = CustomUser.objects.get(email = request.user.email)
    if user.is_organization:
        organization = Organization.objects.get(user = user)
        form = JobPostForm()
        if request.method == 'POST':
            form = JobPostForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                user = CustomUser.objects.get(email = request.user.email)
                organization = Organization.objects.get(user = user)
                form.owner = user
                form.organization_name = organization.name
                form.organization = organization
                form.save()
                return redirect('home')
            else:
                messages.error(request,form.errors)
    else:
        messages.error(request, "You are not authorized to post a job.")

    return render(request, "Job-Post.html", {'form':form })


def Job_Filter_view(request):
    form = None
    pass

def Job_Apply_view(request,pk):

    if request.method == 'POST':
        
        return redirect('home')
    return render(request, "Jobs-Apply.html")

def Notification_Views(request):
    user = CustomUser.objects.get(email = request.user.email)
    message = Notification_model.objects.get(reveiver = user)
    return render(request,"Notification.html",{"message":message})

def Seprate_Message(request,pk):
    if request.method == "POST":
        sender = CustomUser.objects.get(email = request.user.email)
        reveiver = CustomUser.objects.get(id = pk)
        message = request.POST.GET('chat')
        file = request.POST.FILE
        notification = Notification_model.objects.create(sender = sender,reveiver = reveiver,
                                                        message = message,file = file)
        notification.save()
        return redirect('Chat',reveiver.id)
    return render(request, "Seprate-Message.html",{})

def Applited_Job_View(request):
    pass
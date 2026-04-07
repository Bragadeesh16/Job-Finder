from django.contrib.auth import get_user_model
from account.models import Organization
from myapp.models import Jobpost

User = get_user_model()

# 1. Create a dummy organization user
org_email = "hr@google.com"
org_user, created = User.objects.get_or_create(
    email=org_email,
    defaults={
        'is_organization': True,
    }
)
if created:
    org_user.set_password("password123")
    org_user.save()
    print(f"Created organization user: {org_email}")
else:
    print(f"Organization user already exists: {org_email}")

# 2. Create organization profile
org_profile, created = Organization.objects.get_or_create(
    user=org_user,
    defaults={
        'name': "Google",
        'country': "USA",
        'city': "Mountain View",
        'address': "1600 Amphitheatre Parkway",
        'website': "https://google.com",
        'description': "Google is a multinational technology company."
    }
)
if created:
    print("Created Google organization profile.")
else:
    print("Google organization profile already exists.")

# 3. Create dummy jobs
jobs_data = [
    {
        "title": "Software Engineer",
        "description": "Develop high-quality software solutions.",
        "salary": 120000.00,
        "location": "Mountain View, CA",
        "location_type": "Onsite",
        "job_type": "job",
        "employment_type": "full_time",
        "experience_required": "2-3 Year",
        "skills_required": "Python, Django, React"
    },
    {
        "title": "Backend Developer",
        "description": "Design and implement scalable backend services.",
        "salary": 110000.00,
        "location": "Remote",
        "location_type": "Work from home",
        "job_type": "job",
        "employment_type": "full_time",
        "experience_required": "3-4 Year",
        "skills_required": "Python, PostgreSQL, Docker"
    },
    {
        "title": "Frontend Intern",
        "description": "Learn and build interactive user interfaces.",
        "salary": 40000.00,
        "location": "Bengaluru",
        "location_type": "Hybrid",
        "job_type": "internship",
        "employment_type": "part_time",
        "experience_required": "Fresher",
        "skills_required": "HTML, CSS, JavaScript"
    },
    {
        "title": "Data Scientist",
        "description": "Analyze large datasets to drive business insights.",
        "salary": 130000.00,
        "location": "London",
        "location_type": "Onsite",
        "job_type": "job",
        "employment_type": "full_time",
        "experience_required": "5+ Year",
        "skills_required": "Python, Machine Learning, SQL"
    }
]

for job_data in jobs_data:
    job, created = Jobpost.objects.get_or_create(
        title=job_data["title"],
        owner=org_user,
        organization=org_profile,
        defaults={
            "organization_name": org_profile.name,
            "description": job_data["description"],
            "salary": job_data["salary"],
            "location": job_data["location"],
            "location_type": job_data["location_type"],
            "job_type": job_data["job_type"],
            "employment_type": job_data["employment_type"],
            "experience_required": job_data["experience_required"],
            "skills_required": job_data["skills_required"]
        }
    )
    if created:
        print(f"Created job: {job_data['title']}")
    else:
        print(f"Job already exists: {job_data['title']}")

print("Dummy data seeding complete!")

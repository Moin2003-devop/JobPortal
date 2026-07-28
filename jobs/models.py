from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)

    category = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    skills = models.TextField()

    JOB_TYPE = [
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('Onsite', 'Onsite'),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)

    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    description = models.TextField()

    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant_name
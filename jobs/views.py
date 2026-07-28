from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Job, Application
from .forms import ApplicationForm


def job_list(request):
    search = request.GET.get("search")
    location = request.GET.get("location")
    category = request.GET.get("category")
    job_type = request.GET.get("job_type")

    jobs = Job.objects.all().order_by("-posted_on")

    if search:
        jobs = jobs.filter(
            Q(title__icontains=search) |
            Q(company__icontains=search)
        )

    if location:
        jobs = jobs.filter(location__icontains=location)

    if category:
        jobs = jobs.filter(category__icontains=category)

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    return render(request, "jobs.html", {
        "jobs": jobs
    })


def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()

            return redirect("job_list")

    else:
        form = ApplicationForm()

    return render(request, "apply.html", {
        "form": form,
        "job": job
    })


def dashboard(request):
    applications = Application.objects.select_related("job")

    return render(request, "dashboard.html", {
        "applications": applications
    })
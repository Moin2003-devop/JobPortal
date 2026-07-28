from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "location",
        "job_type",
        "posted_on",
    )

    search_fields = (
        "title",
        "company",
        "location",
    )

    list_filter = (
        "job_type",
        "category",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "applicant_name",
        "email",
        "job",
        "created_at",
    )

    search_fields = (
        "applicant_name",
        "email",
    )
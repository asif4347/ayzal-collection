from django.db import models


# Create your models here.
class Subscription(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Contacts(models.Model):
    subjects = (
        ("Need help with", ""),
        ("New Project", "New Project"),
        ("Existing Project", "Existing Project")
    )
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=False, null=False)
    comment = models.TextField(null=False, blank=False, max_length=500)
    # requirements_doc = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

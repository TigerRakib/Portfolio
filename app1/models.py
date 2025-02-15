from django.db import models
class contact_form_info(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField()
    action_time=models.DateTimeField()
    is_error=models.BooleanField(default=False)
    is_success=models.BooleanField(default=False)
    error_message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.email
# Create your models here.

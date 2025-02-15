from django.contrib import admin
from app1.models import contact_form_info
@admin.register(contact_form_info)
class contact_form_infoAdmin(admin.ModelAdmin):
    list_display=[
        "email",
        "is_error",
        "is_success",
        "action_time"
    ]
#<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3634.5095000748684!2d88.62580237506616!3d24.363573164960872!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39fbefd0a55ea957%3A0x2f9cac3357d62617!2sRajshahi%20University%20of%20Engineering%20%26%20Technology(RUET)!5e0!3m2!1sen!2sbd!4v1739567060065!5m2!1sen!2sbd" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
# Register your models here.

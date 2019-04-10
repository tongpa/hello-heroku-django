from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from hello_app.models import Service
from hello_app.services.sendmailservice import sendmail


@receiver(post_save, sender=Service)
def checkServiceCustomer(sender, instance,created, **kwargs):
    if created:
        subject = "%s" %(instance.insure_type)
        message = "%s ของ %s สนใจ %s \n ประเภทรภ : %s\n ทะเบียน : %s\n %s" \
                  %(instance.customer, instance.agent, instance.insure_type, instance.car_type, instance.license_plate,instance.remark )


        sendmail(subject ,message ,send_to='tongmakchu@gmail.com')

from django.db.models.signals import post_save
from users.models import User, Student, Staff
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "ADMIN" or instance.user_type == "HOD" or instance.user_type == "STAFF":
            Staff.objects.create(user=instance)
        elif instance.user_type == "REPRESENTATIVE" or instance.user_type == "STUDENT":
            Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_student(sender, instance, created, **kwargs):
    if instance.user_type == "ADMIN" or instance.user_type == "HOD" or instance.user_type == "STAFF":
        instance.staff.save()
    elif instance.user_type == "REPRESENTATIVE" or instance.user_type == "STUDENT":
        instance.student.save()
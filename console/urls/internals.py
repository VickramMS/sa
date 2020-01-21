from django.urls import path
from console.views import internals

urlpatterns = [
    path('enroll_internal/', internals.enroll_internal, name='enroll_internal'),
    path('internals/', internals.internals, name='internals'),
    path('finish_int/', internals.finish_int, name='finish_int'),
    path('finish_int/<id>/<id2>/', internals.delete_int, name='delete_int'),
    path('finish_int/<id>/<id2>/delete/', internals.delete_internal, name='delete_internal'),
    path('assigned_class/', internals.assigned_int, name='assigned_class'),
    path('assign_int/', internals.assign_int, name='assign_int'),
]
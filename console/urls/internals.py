from django.urls import path
from console.views import internals

urlpatterns = [
    path('assign_internals/', internals.assign_internals, name='assign_internals'),
    path('enroll_internals/', internals.enroll_internal, name='enroll_internal'),
    path('internals/', internals.internals, name='internals'),
    path('finish_internals/', internals.finish_internals, name='finish_int'),
    path('finish_internals/<id>/<id2>/', internals.delete_internal, name='delete_int'),
    path('finish_internals/<id>/<id2>/delete/', internals.delete_internals, name='delete_internal'),
    path('assigned_internals/', internals.assigned_internals, name='assigned_class'),
]
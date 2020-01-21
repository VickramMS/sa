from django.urls import path
from console.views import internals

urlpatterns = [
    path('academics/internals/', internals.internals, name='internals'),
    path('academics/finish_int/', internals.finish_int, name='finish_int'),
    path('academics/finish_int/<id>/<id2>/', internals.delete_int, name='delete_int'),
    path('academics/finish_int/<id>/<id2>/delete/', internals.delete_internal, name='delete_internal'),
    path('academics/assigned_class/', internals.assigned_int, name='assigned_class'),
    path('jobs/assign_int/', internals.assign_int, name='assign_int'),
    path('jobs/enroll_internal/', internals.enroll_internal, name='enroll_internal'),
]
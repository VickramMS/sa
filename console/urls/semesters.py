from django.urls import path
from console.views import semesters

urlpatterns=[
    path('assign_semester/', semesters.assign_semesters, name='assign_semesters'),
    path('enroll_semester/', semesters.enroll_semester, name='enroll_semester'),
    path('semesters/', semesters.semesters, name='semesters'),
    path('finish_semesters/', semesters.finish_semesters, name='finish_sem'),
    path('finish_semesters/<id>/<id2>/', semesters.delete_semester, name='delete_sem'),
    path('finish_semesters/<id>/<id2>/delete/', semesters.delete_semesters, name='delete_semester'),
    path('assigned_semesters/', semesters.assigned_semesters, name='assigned_sem'),
]
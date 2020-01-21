from django.urls import path
from console.views import semesters

urlpatterns=[
    path('academics/semesters/', semesters.semesters, name='semesters'),
    path('academics/finish_sem/', semesters.finish_sem, name='finish_sem'),
    path('academics/finish_sem/<id>/<id2>/', semesters.delete_sem, name='delete_sem'),
    path('academics/finish_sem/<id>/<id2>/delete/', semesters.delete_semester, name='delete_semester'),
    path('academics/assigned_sem/', semesters.assigned_sem, name='assigned_sem'),
    path('jobs/assign_sem/', semesters.assign_sem, name='assign_sem'),
    path('jobs/enroll_semester/', semesters.enroll_semester, name='enroll_semester'),
]
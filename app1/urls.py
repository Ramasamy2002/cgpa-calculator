from django.urls import path
from . import views

urlpatterns=[
    path('',views.homeRe,name='sample'),
    path('calc/',views.sample,name="sample"),
    path('calc/fetch/',views.fetch,name="fetch"),
    path('calc/delete/<int:id>',views.delete,name="delete"),
    path('calc/cgpa/',views.sample2,name="sample2"),
    path('calc/cgpa/fetchh/',views.fetchh,name="fetchh"),
    path('calc/cgpa/deletee/<int:id>',views.deletee,name="deletee"),
    path('calc/cgpa/revert/',views.revert,name="revert"),
]

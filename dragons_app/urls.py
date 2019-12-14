from django.urls import path, include
from django.conf.urls import url
from dragons_app import views

urlpatterns=[
    path('rules/', views.RuleView.as_view()),
    path('delete-rule/<int:pk>/', views.DeleteRuleView.as_view()),
    path('dragons/', views.DragonView.as_view()),
    path('kill_by_dragon/', views.kill_by_dragon),
]
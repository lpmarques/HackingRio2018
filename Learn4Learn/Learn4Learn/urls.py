"""Learn4Learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from core import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^home/', views.home, name='home'),
	url(r'^cursos/novo/', views.new_course, name='new_course'),
	url(r'^cursos/(?P<course_id>[0-9]+)/$', views.manage_course, name = 'manage_course'),
	url(r'^cursos/(?P<course_id>[0-9]+)/remover/$', views.remove_course, name = 'remove_course'),
	url(r'^cursos/(?P<course_id>[0-9]+)/competencias/nova', views.new_skill, name = 'new_skill'),
	url(r'^cursos/(?P<course_id>[0-9]+)/competencias/(?P<skill_id>[0-9]+)/remover', views.remove_skill, name = 'remove_skill'),
	url(r'^cursos/(?P<course_id>[0-9]+)/alunos/(?P<student_id>[0-9]+)/$', views.manage_student, name = 'manage_student'),
	url(r'^cursos/(?P<course_id>[0-9]+)/alunos/(?P<student_id>[0-9]+)/remover', views.remove_student, name = 'remove_student'),
	url(r'^cursos/(?P<curso_id>[0-9]+)?/novoaluno', views.new_student, name = 'new_student'),
    url(r'^admin/', admin.site.urls),
]

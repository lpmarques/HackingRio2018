# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader

from django.http import HttpResponseRedirect, HttpResponse

from .forms import LoginForm, NewCourse

from models import Teacher, Course

#from .models import *

# Create your views here.

#def index( request ):
#	#return HttpResponse("teste")
#	template = loader.get_template('core/index.html')
#	context = { 'default_user': "teste" }
#	return HttpResponse( template.render( context, request ) )
	
def index(request):
	#Valida o formulário e confere se a foi uma solitação de POST
	if request.method == 'POST' and LoginForm(request.POST).is_valid():
		#Redireciona para a view responsável por validar o login
		if login(request.POST.get( "user" ), request.POST.get( "password" ) ):
			request.session['user'] = request.POST.get( "user" )
			return HttpResponseRedirect('/home/')
	return render( request, 'core/login.html', { 'form': LoginForm() } )

def login( _user, _password):
	try:
		teacher = Teacher.objects.get(user = _user, password = _password)
		return True
	except Teacher.DoesNotExist:
		return False
	
def home(request):
	course_list = Course.objects.all()
	template = loader.get_template('core/home.html')
	context = { 'course_list': course_list}
	return render(request, 'core/home.html', context)

def new_course(request):
	#Valida o formulário e confere se a foi uma solitação de POST
	if request.method == 'POST' and NewCourse(request.POST).is_valid():
		#Cadastra um novo curso
		course = Course(name = request.POST.get( "name" ), professor = Teacher.objects.get(user = request.session['user']) )
		course.save()
		return HttpResponseRedirect('/home/novo/')
	return render( request, 'core/new_course.html', { 'form': NewCourse() } )

def new_student(request):
	if request.method == 'POST' and NewStudent(request.POST).is_valid():
		student = Student(name = request.POST.get( "name" ))
		student.save()
		return HttpResponseRedirect('/home/cursos/(?P<curso_id>[0-9]+)/')
	return render( request, 'core/new_student.html' { 'form': NewStudent() } )

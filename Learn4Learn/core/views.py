# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader

from django.http import HttpResponseRedirect, HttpResponse

from .forms import *

from models import *

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

def remove_course(request, course_id):
	try:
		course = Course.objects.get(id = int( course_id ) )
		course.delete()
	except Course.DoesNotExist:
		return HttpResponseRedirect('/home/')
	return HttpResponseRedirect('/home/')	
	
	
def manage_course(request, course_id):
	try:
		student_list = Student.objects.filter( course = Course.objects.get( id =  int(course_id)) )
	except Student.DoesNotExist:
		student_list = {}
	try:
		skill_list = Skill.objects.filter( course = Course.objects.get( id =  int(course_id)) )
	except Skill.DoesNotExist:
		skill_list = {}
	context = {'student_list': student_list, 'course_id': course_id, 'skill_list': skill_list}
	return render(request, 'core/course_details.html', context)

def new_student(request, curso_id):
	if request.method == 'POST' and NewStudent(request.POST).is_valid():
		student = Student(name = request.POST.get( "name" ))
		student.save()
		student.course.add( Course.objects.get( id =  int(curso_id)) )
		student.save()
		return HttpResponseRedirect('/cursos/%s/' % curso_id)
	return render( request, 'core/new_student.html', { 'form': NewStudent(), 'course_id': curso_id } )

def remove_student(request, course_id, student_id):
	try:
		student = Student.objects.get(id = int( student_id ) )
		student.course.remove( Course.objects.get( id =  int(course_id)) )
	except Student.DoesNotExist:
		return HttpResponseRedirect('/cursos/%s/' % course_id)
	return HttpResponseRedirect('/cursos/%s/' % course_id)
	
def new_skill(request, course_id):
	if request.method == 'POST' and NewSkill(request.POST).is_valid():
		skill = Skill( name = request.POST.get( "name" ) )
		skill.course = Course.objects.get( id =  int(course_id) )
		skill.save()
		return HttpResponseRedirect('/cursos/%s/' % course_id)
	return render( request, 'core/new_skill.html', { 'form': NewSkill(), 'course_id': course_id } )

def remove_skill(request, course_id, skill_id):
	try:
		skill = Skill.objects.get(id = int( skill_id ) )
		skill.delete()
	except Skill.DoesNotExist:
		return HttpResponseRedirect('/cursos/%s/' % course_id)
	return HttpResponseRedirect('/cursos/%s/' % course_id)

def manage_student(request, student_id, course_id):
	try:
		grades_list = ScoreRecord.objects.filter( student = Student.objects.get( id = int(student_id), course = Course.objects.get( id = int(course_id) )) )
	except ScoreRecord.DoesNotExist:
		grades_list = {}
	context = {'grades_list': grades_list, 'student_id': student_id, 'course_id': course_id}
	return render( request, 'core/student_details.html', context)
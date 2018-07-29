# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Teacher(models.Model):
	id = models.AutoField( primary_key = True )
	name = models.CharField( max_length = 100 )
	user = models.CharField( max_length = 100 )
	password = models.CharField( max_length = 7 )
	def __str__(self):
		return self.name
	
@python_2_unicode_compatible
class Course(models.Model):
	professor = models.ForeignKey( Teacher, on_delete = models.CASCADE )
	name = models.CharField( max_length = 100 , default = "sem_nome")
	def __str__(self):
		return self.name
		
@python_2_unicode_compatible
class Skill(models.Model):
	skill = models.CharField( max_length = 300 )
	def __str__(self):
		return self.skill

@python_2_unicode_compatible	
class SkillIndex(models.Model):
	skill = models.ForeignKey( Skill, on_delete = models.CASCADE )
	grade = models.DecimalField( max_digits = 4, decimal_places = 2 )
	def __str__(self):
		return self.skill.skill
		
@python_2_unicode_compatible
class Student(models.Model):
	id = models.AutoField( primary_key = True )
	name = models.CharField( max_length = 100 )
	user = models.CharField( max_length = 100 )
	password = models.CharField( max_length = 7 )
	course = models.ManyToManyField( Course )
	def __str__(self):
		return self.name
		
@python_2_unicode_compatible		
class ScoreRecord(models.Model):
	student = models.ForeignKey( Student, on_delete = models.CASCADE )
	course = models.ForeignKey( Course, on_delete = models.CASCADE )
	skill_index = models.ManyToManyField( SkillIndex )
	total_grade = models.DecimalField(max_digits = 4, decimal_places = 2 )
	def __str__(self):
		return "%s | %s | %.2f" % (self.student, self.course, self.total_grade)

		
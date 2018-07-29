from django import forms

class LoginForm(forms.Form):
	user = forms.CharField( label = ' usuario', max_length = 15 )
	password = forms.CharField( label = 'password', max_length = 8 )
	
class NewCourse(forms.Form):
	name = forms.CharField( label = ' Nome do curso ', max_length = 100 )
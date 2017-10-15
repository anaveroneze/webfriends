#coding: utf-8
# from registration.views import RegistrationView
from registration.backends.default.views import RegistrationView
from django.conf.urls import url
from experiment.forms import UsuarioFriendsForm
from experiment.models import UsuarioFriends
from django.contrib import messages

class MyRegistrationView(RegistrationView):

	form_class = UsuarioFriendsForm

	def register(self, form_class):
		new_user = super(MyRegistrationView,self).register(form_class)
		user_profile = UsuarioFriends()
		user_profile.usuario = new_user
		user_profile.nickname = form_class.cleaned_data['nickname']
		user_profile.company = form_class.cleaned_data['company']
		user_profile.save()
		return user_profile

	def get_success_url(self, user):
		return render_to_response('login.html', message='Save complete')
		#return '/login/'

# from registration.views import RegistrationView
from registration.backends.default.views import RegistrationView
from experiment.forms import UsuarioFriendsForm
from experiment.models import UsuarioFriends
from django.contrib import messages
from django.http import HttpResponse
from django.core.urlresolvers import reverse

class MyRegistrationView(RegistrationView):

	form_class = UsuarioFriendsForm

	def register(self,request, form_class):
		new_user = super(MyRegistrationView,self).register(request,form_class)
		user_profile = UsuarioFriends()
		user_profile.usuario = new_user
		user_profile.nickname = form_class.cleaned_data['nickname']
		user_profile.company = form_class.cleaned_data['company']
		user_profile.save()
		messages.add_message(request, messages.INFO, 'Yeehaw!')
		return HttpResponseRedirect(reverse('login'))

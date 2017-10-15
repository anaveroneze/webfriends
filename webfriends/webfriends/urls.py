from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import regbackend
from django.views.generic.base import TemplateView

urlpatterns = [
    # urls experiment
    url(r'^$', 'experiment.views.home', name='home'),
    url(r'^about/$', 'experiment.views.about', name='about'),
    url(r'^contact/$', 'experiment.views.contact', name='contact'),
    url(r'^experiments/checkForm$',
        'experiment.views.checkForm', name='checkForm'),
    url(r'^experiments/$', 'experiment.views.experiments', name='exp'),
    url(r'^experiments/remove$', 'experiment.views.experimentsRemove', name='expRemove'),
    url(r'^experiments/downloadInputFile', 'experiment.views.downloadInputFile',
        name='downloadInputFile'),
    url(r'^experiments/downloadOutputFile', 'experiment.views.downloadOutputFile',
        name='downloadOutputFile'),

    #django admin
    url(r'^experiments/result$', 'experiment.views.result', name='result'),
    url(r'^admin/', include(admin.site.urls)),

    # urls register
    url(r'^accounts/register/', regbackend.MyRegistrationView.as_view(),
        name='register_custom'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    
    url(r'^register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'),name='registration_disallowed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

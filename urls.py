from django.conf.urls.defaults import patterns, include, url
from per_ac.views import *
from per_ac.users.views import *
from per_ac.category.views import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	 url(r'^$',welcome),
    url(r'^registr/$', registr),
    url(r'^welcome/$', welcome),
    url(r'^login/$', login),
    url(r'^new_cat/$',AddCat),
    url(r'^view_cat/$',ViewCat),
    url(r'^logout/$', logout),
    url(r'^main/$', main_menu),
    url(r'^edit_cat/$', EditCat),
    url(r'^add_payment/$', AddPayment),
    url(r'^edit_profile/$', edit_user_profile), 
#    url(r'^q/$', contact),
    # Examples:
    # url(r'^$', 'per_ac.views.home', name='home'),
    # url(r'^per_ac/', include('per_ac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
    )

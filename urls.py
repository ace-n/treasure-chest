from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('treasureapp.views',
    # Treasureapp URLs

    # Account management URLs
    url(r'^account/(?P<account_id>\d+)/update$', 'account_update', {}, 'account_update'),
    url(r'^account/(?P<account_id>\d+)$', 'account_detail', {}, 'account_detail'),
    url(r'^account/new$', 'account_create', {}, 'account_create'),
    url(r'^account/$', 'account_list', {}, 'account_list'),
    url(r'^account/(?P<label_filter>.+)$', 'account_list', {}, 'account_list'),

    # Transaction management URLs
    url(r'^account/(?P<account_id>\d+)/transaction/new$', 'transaction_create', {}, 'transaction_create'),
    url(r'^transaction/(?P<transaction_id>\d+)/update$', 'transaction_update', {}, 'transaction_update'),
    url(r'^transaction/(?P<transaction_id>\d+)$', 'transaction_detail', {}, 'transaction_detail'),

    # Group management URLs
    url(r'^group/(?P<group_id>\d+)/update$', 'group_update', {}, 'group_update'),
    url(r'^group/(?P<group_id>\d+)$', 'group_detail', {}, 'group_detail'),
    url(r'^group/new$', 'group_create', {}, 'group_create'),
    url(r'^group/$', 'group_manager', {}, 'group_manager'),

    # Label URLs
    url(r'^label/$', 'label_list', {}, 'label_list'),
    url(r'^label/new$', 'label_create', {}, 'label_create'),

    # Site standard content URLs
    url(r'^help$', 'help', {}, 'help'),
    url(r'^$', 'index', {}, 'index'),
)

urlpatterns += patterns('',
    # Registration controls
    (r'^', include('registration.backends.default.urls')),
    (r'^', include('registration.auth_urls')),
    # Administration controls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        # Static files (development server only)
        (r'^assets/(?P<path>.*)', 'django.views.static.serve',
            { 'document_root' : settings.ASSETS_ROOT })
    )

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bams.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','codes.views.index',name="index"),

    url(r'^codes/(?P<code_id>\d+)/edit/(?P<id>\d+)$','codes.views.edit_code',name="edit_code"),
    url(r'^codes/(?P<code_id>\d+)/add$','codes.views.add',name="code_add"),
    url(r'^codes/(?P<code_id>\d+)/edit$','codes.views.edit',name="code_edit"),
    url(r'^codes/','codes.views.codes',name="codes"),

    url(r'^rates/(?P<rate_id>\d+)/edit','rate.views.edit_rate',name="edit_rate"),
    url(r'^rates/add','rate.views.add_rate',name="add_rate"),
    url(r'^rates/','rate.views.index',name="rates_index"),

]

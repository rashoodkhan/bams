from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bams.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','codes.views.index',name="index"),
    url(r'^codes/(?P<code_id>\d+)/add$','codes.views.add',name="code_add"),
    url(r'^codes/(?P<code_id>\d+)/edit$','codes.views.edit',name="code_edit"),
    url(r'^codes/','codes.views.codes',name="codes"),

]

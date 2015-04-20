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
    url(r'^rates/?','rate.views.index',name="rates_index"),

    url(r'^survey/(?P<building_id>\d+)/edit/(?P<survey_id>\d+)/?','survey.views.edit_building_data',name="edit_building_data"),
    url(r'^survey/(?P<building_id>\d+)/add/?','survey.views.add_building_data',name="add_building_data"),
    url(r'^survey/(?P<building_id>\d+)/?','survey.views.building_survey',name="building_survey"),
    url(r'^survey/add','survey.views.add_survey',name="add_survey"),
    url(r'^survey/?','survey.views.index',name="survey_index"),

    url(r'^reports/(?P<type_id>\d+)/(?P<report_id>\d+)/?','reports.views.getSurveyForm',name="getSurveyForm"),
    url(r'^reports/?','reports.views.index',name="reports_index"),

]

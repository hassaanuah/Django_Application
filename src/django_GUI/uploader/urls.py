from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^captive_portal/$', views.captive_portal, name='captive_portal'),



    url(r'^table_view/ID/$', views.view_table, {'database_specified': 'ces', 'table_specified': 'ID'}, name='view_table'),
    url(r'^table_view/FIREWALL/$', views.view_table, {'database_specified': 'ces', 'table_specified': 'FIREWALL'}, name='view_table'),
    url(r'^table_view/HOST_POLICY_IDENTITY/$', views.view_table, {'database_specified': 'ces', 'table_specified': 'HOST_POLICY_IDENTITY'}, name='view_table'),
    url(r'^table_view/HOST_POLICIES/$', views.view_table, {'database_specified': 'ces', 'table_specified': 'HOST_POLICIES'}, name='view_table'),
    url(r'^table_view/CES_POLICY_IDENTITY/$', views.view_table, {'database_specified': 'ces', 'table_specified': 'CES_POLICY_IDENTITY'}, name='view_table'),
    url(r'^table_view/CES_POLICIES/$', views.view_table, {'database_specified': 'ces', 'table_specified': 'CES_POLICIES'}, name='view_table'),

    url(r'^table_view/ID/(?P<id>\d+)/$', views.edit_entry, {'database_specified': 'ces', 'table_specified': 'ID'}, name='edit_entry'),
    url(r'^table_view/FIREWALL/(?P<id>\d+)/$', views.edit_entry, {'database_specified': 'ces', 'table_specified': 'FIREWALL'}, name='edit_entry'),
    url(r'^table_view/HOST_POLICY_IDENTITY/(?P<id>\d+)/$', views.edit_entry, {'database_specified': 'ces', 'table_specified': 'HOST_POLICY_IDENTITY'}, name='edit_entry'),
    url(r'^table_view/HOST_POLICIES/(?P<id>\d+)/$', views.edit_entry, {'database_specified': 'ces', 'table_specified': 'HOST_POLICIES'}, name='edit_entry'),
    url(r'^table_view/CES_POLICY_IDENTITY/(?P<id>\d+)/$', views.edit_entry, {'database_specified': 'ces', 'table_specified': 'CES_POLICY_IDENTITY'}, name='edit_entry'),
    url(r'^table_view/CES_POLICIES/(?P<id>\d+)/$', views.edit_entry, {'database_specified': 'ces', 'table_specified': 'CES_POLICIES'}, name='edit_entry'),

    url(r'^entry/ID/$', views.add_table_page, {'database_specified': 'ces', 'table_specified': 'ID'}, name='add_table_page'),
    url(r'^entry/FIREWALL/$', views.add_table_page, {'database_specified': 'ces', 'table_specified': 'FIREWALL'}, name='add_table_page'),
    url(r'^entry/HOST_POLICY_IDENTITY/$', views.add_table_page, {'database_specified': 'ces', 'table_specified': 'HOST_POLICY_IDENTITY'}, name='add_table_page'),
    url(r'^entry/HOST_POLICIES/$', views.add_table_page, {'database_specified': 'ces', 'table_specified': 'HOST_POLICIES'}, name='add_table_page'),
    url(r'^entry/CES_POLICY_IDENTITY/$', views.add_table_page, {'database_specified': 'ces', 'table_specified': 'CES_POLICY_IDENTITY'}, name='add_table_page'),
    url(r'^entry/CES_POLICIES/$', views.add_table_page, {'database_specified': 'ces', 'table_specified': 'CES_POLICIES'}, name='add_table_page'),



    url(r'^table_view/bootstrap/$', views.view_table, {'database_specified': 'bootstrap', 'table_specified': 'bootstrap'}, name='view_table'),
    url(r'^entry/bootstrap/$', views.add_table_page, {'database_specified': 'bootstrap', 'table_specified': 'bootstrap'}, name='add_table_page'),
    url(r'^table_view/bootstrap/(?P<id>\d+)/$', views.edit_entry, {'database_specified': 'bootstrap', 'table_specified': 'bootstrap'}, name='edit_entry'),



    url(r'^user_registration/$', views.user_registration, name='user_registration'),
    url(r'^$', views.main, name='main'),
]


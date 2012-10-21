#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from views import ListView, DetailView, CreateView, UpdateView, \
    CapacitacionCreateView, PruebaCreateView, PreguntaCreateView
from django.contrib.auth.decorators import login_required
from elearning.models import Capacitacion, Prueba, Pregunta
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User


capacitacion_patterns = patterns(
    '',
    url(
        r'^index/(?P<page>[0-9]+)/(\?.*)?$',
        ListView.as_view(
            model=Capacitacion,
            template_name='capacitacion/index.html',
            paginate_by=10,
            context_object_name='capacitacion_list',
        ), name='index'
    ),
    url(
        r'^detalle/(?P<pk>[0-9]+)/(\?.*)?$',
        DetailView.as_view(
            model=Capacitacion,
            template_name='capacitacion/detalle.html',
            context_object_name='capacitacion',
        ), name='detalle'
    ),
    url(
        r'^nuevo/(\?.*)?$',
        CapacitacionCreateView.as_view(
            model=Capacitacion,
            template_name='capacitacion/form.html',
            context_object_name='capacitacion',
        ), name='nuevo'
    ),
    url(
        r'^editar/(?P<pk>[0-9]+)/(\?.*)?$',
        UpdateView.as_view(
            model=Capacitacion,
            template_name='capacitacion/form.html',
            context_object_name='capacitacion',
        ), name='editar'
    ),
    url(
        r'^editar/(?P<pk>[0-9]+)/profesor/agregar/(\?.*)?$',
        DetailView.as_view(
            model=User,
            template_name='capacitacion/add_profesor.html',
            context_object_name='capacitacion',
        ), name='add_profesor'
    ),
    url(
        r'^editar/(?P<cap_id>[0-9]+)/profesor/agregar/(?P<user_id>[0-9]+)/(\?.*)?$',
        'elearning.views.agregar_profesor'
    ),
    url(
        r'^editar/(?P<cap_id>[0-9]+)/profesor/remover/(?P<user_id>[0-9]+)/(\?.*)?$',
        'elearning.views.remover_profesor'
    ),
    url(
        r'^editar/(?P<pk>[0-9]+)/alumno/agregar/(\?.*)?$',
        DetailView.as_view(
            model=Capacitacion,
            template_name='capacitacion/add_alumno.html',
            context_object_name='capacitacion',
        ), name='add_profesor'
    ),
    url(
        r'^editar/(?P<cap_id>[0-9]+)/alumno/agregar/(?P<user_id>[0-9]+)/(\?.*)?$',
        'elearning.views.agregar_alumno'
    ),
    url(
        r'^editar/(?P<cap_id>[0-9]+)/alumno/remover/(?P<user_id>[0-9]+)/(\?.*)?$',
        'elearning.views.remover_alumno'
    ),
    url(
        r'^eliminar/(?P<pk>[0-9]+)/(\?.*)?$',
        'elearning.views.remover_capacitacion'
    ),
    url(
        r'^(?P<pk>[0-9]+)/prueba/nuevo/(\?.*)?$',
        PruebaCreateView.as_view(
            model=Prueba,
            template_name='prueba/form.html',
            context_object_name='prueba',
        ), name='nuevo'
    )
)

prueba_patterns = patterns(
    '',
    url(
        r'^index/(?P<page>[0-9]+)/(\?.*)?$',
        login_required(
            ListView.as_view(
                model=Prueba,
                template_name='prueba/index.html',
            )
        ), name='index'
    ),
    url(
        r'^detalle/(?P<pk>[0-9]+)/(\?.*)?$',
        login_required(
            DetailView.as_view(
                model=Prueba,
                template_name='prueba/detalle.html',
            )
        ), name='detalle'
    ),
    url(
        r'^nuevo/(?P<pk>[0-9]+)/(\?.*)?$',
        login_required(
            PruebaCreateView.as_view(
                model=Prueba,
                template_name='prueba/form.html',
            )
        ), name='nuevo'
    ),
    url(
        r'^editar/(?P<pk>[0-9]+)/(\?.*)?$',
        login_required(
            UpdateView.as_view(
                model=Prueba,
                template_name='prueba/form.html',
            )
        ), name='editar'
    )
)

pregunta_patterns = patterns(
    '',
    url(
        r'^index/(?P<page>[0-9]+)/(\?.*)?$',
        login_required(
            ListView.as_view(
                model=Prueba,
                template_name='prueba/index.html',
            )
        ), name='index'
    ),
    url(
        r'^detalle/(?P<pk>[0-9]+)/(\?.*)?$',
        login_required(
            DetailView.as_view(
                model=Prueba,
                template_name='prueba/detalle.html',
            )
        ), name='detalle'
    ),
    url(
        r'^nuevo/(?P<pk>[0-9]+)/(\?.*)?$',
        login_required(
            PreguntaCreateView.as_view(
                model=Pregunta,
                template_name='pregunta/form.html',
            )
        ), name='nuevo'
    ),
    url(
        r'^editar/(?P<pk>[0-9]+)/(\?.*)?$',
        login_required(
            UpdateView.as_view(
                model=Prueba,
                template_name='prueba/form.html',
            )
        ), name='editar'
    )
)

urlpatterns = patterns(
    '',
    url(
        r'^$',
        login_required(
            ListView.as_view(
                model=Capacitacion,
                template_name='capacitacion/index.html',
            )
        )
    ),
    url(
        r'^login/$', login, {'template_name': 'login.html'}
    ),
    url(
        r'^logout/$', logout, {'next_page': '/login'}
    ),
    url(
        r'^capacitacion/',
        include(capacitacion_patterns, namespace='capacitacion')
    ),
    url(
        r'^prueba/',
        include(prueba_patterns, namespace='prueba')
    ),
    url(
        r'^pregunta/',
        include(pregunta_patterns, namespace='pregunta')
    )
)

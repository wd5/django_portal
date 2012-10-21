#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.utils.decorators import method_decorator
from elearning.models import Capacitacion
import datetime


def escalenoContext(context, user):
    profesores = User.objects.filter(groups__name='Profesor')
    alumnos = User.objects.filter(groups__name='Alumno')
    capacitaciones_usuario = set(user.alumnos.all())
    capacitaciones = set(Capacitacion.objects.all())
    rendidas = capacitaciones_usuario & capacitaciones
    pendientes = capacitaciones - capacitaciones_usuario
    empresa = {
        'nombre': 'Entel S.A.',
        'url': 'www.entel.cl',
        'gerencia': 'Gerencia Departamento Atencion Tecnica Territorial',
        'sigla': 'ATT', }

    context['usuario'] = user
    context['capacitaciones_usuario'] = len(capacitaciones_usuario)
    context['rendidas'] = len(rendidas)
    context['pendientes'] = len(pendientes)
    context['empresa'] = empresa
    context['profesores'] = profesores
    context['alumnos'] = alumnos
    if Group.objects.get(name='Profesor') in user.groups.all():
        context['profesor'] = True

    return context


class ListView(ListView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)

        return escalenoContext(context, self.request.user)


class DetailView(DetailView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        return escalenoContext(context, self.request.user)


class CreateView(CreateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse(
            'elearning:capacitacion:index', args=(1, ))

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)

        return escalenoContext(context, self.request.user)


class CapacitacionCreateView(CreateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacitacionCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse(
            'elearning:capacitacion:index', args=(1, ))

    def get_context_data(self, **kwargs):
        context = super(CapacitacionCreateView, self).get_context_data(**kwargs)

        return escalenoContext(context, self.request.user)

    def get_initial(self):
        initial = super(CapacitacionCreateView, self).get_initial()
        initial = initial.copy()
        initial['docentes'] = [self.request.user, ]
        return initial


class UpdateView(UpdateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse(
            'elearning:capacitacion:index', args=(1, ))

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)

        return escalenoContext(context, self.request.user)


@login_required
def agregar_profesor(request, cap_id, user_id):

    capacitacion = get_object_or_404(Capacitacion, pk=cap_id)
    usuario = get_object_or_404(User, pk=user_id)
    if usuario not in capacitacion.docentes.all():
        capacitacion.docentes.add(usuario)
        capacitacion.save()
    else:
        messages.error(request, 'El docente no fue agregado')

    return HttpResponseRedirect('/capacitacion/detalle/'
                                + str(capacitacion.id))


@login_required
def remover_profesor(request, cap_id, user_id):

    capacitacion = get_object_or_404(Capacitacion, pk=cap_id)
    usuario = get_object_or_404(User, pk=user_id)
    if len(capacitacion.docentes.all()) > 1:
        if usuario in capacitacion.docentes.all():
            capacitacion.docentes.remove(usuario)
            capacitacion.save()
        else:
            messages.error(request, 'El docente no fue removido')
    else:
        messages.error(request, 'La capacitacion no puede quedar sin docente')

    return HttpResponseRedirect('/capacitacion/detalle/'
                                + str(capacitacion.id))


@login_required
def agregar_alumno(request, cap_id, user_id):

    capacitacion = get_object_or_404(Capacitacion, pk=cap_id)
    usuario = get_object_or_404(User, pk=user_id)
    if usuario not in capacitacion.alumnos.all():
        capacitacion.alumnos.add(usuario)
        capacitacion.save()
    else:
        messages.error(request, 'El alumno no fue agregado')

    return HttpResponseRedirect('/capacitacion/detalle/'
                                + str(capacitacion.id))


@login_required
def remover_alumno(request, cap_id, user_id):

    capacitacion = get_object_or_404(Capacitacion, pk=cap_id)
    usuario = get_object_or_404(User, pk=user_id)
    if usuario in capacitacion.alumnos.all():
        capacitacion.alumnos.remove(usuario)
        capacitacion.save()
    else:
        messages.error(request, 'El alumno no fue removido')

    return HttpResponseRedirect('/capacitacion/detalle/'
                                + str(capacitacion.id))


@login_required
def remover_capacitacion(request, pk):

    capacitacion = get_object_or_404(Capacitacion, pk=pk)
    capacitacion.delete()

    return HttpResponseRedirect('/capacitacion/index/1')


class PruebaCreateView(CreateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PruebaCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        print self.object.pk
        print self.object.id
        return reverse(
            'elearning:prueba:editar', kwargs={'pk': self.object.pk, })

    def get_context_data(self, **kwargs):
        context = super(PruebaCreateView, self).get_context_data(**kwargs)
        context['capacitacion'] = get_object_or_404(Capacitacion, pk=self.kwargs['pk'])
        return escalenoContext(context, self.request.user)

    def get_initial(self):
        initial = super(PruebaCreateView, self).get_initial()
        initial = initial.copy()
        initial['capacitacion'] = self.kwargs['pk']
        return initial


class PreguntaCreateView(CreateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PreguntaCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse(
            'elearning:capacitacion:add_pregunta', kwargs={'pk': self.object.pk},)

    def get_context_data(self, **kwargs):
        context = super(PreguntaCreateView, self).get_context_data(**kwargs)
        context['capacitacion'] = get_object_or_404(Capacitacion, pk=self.kwargs['pk'])
        return escalenoContext(context, self.request.user)

    def get_initial(self):
        initial = super(PreguntaCreateView, self).get_initial()
        initial = initial.copy()
        initial['capacitacion'] = self.kwargs['pk']
        initial['fecha_creacion'] = datetime.date.today()
        return initial

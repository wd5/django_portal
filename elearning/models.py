#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
import datetime
from django.contrib.auth.models import User


class UserProfile(models.Model):

    rut = models.CharField(max_length=200)
    usuario = models.OneToOneField(User)

    def __unicode__(self):
        return u'%s %s' % (self.usuario.first_name, self.usuario.last_name)


class Capacitacion(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    contenido = models.TextField(blank=True)
    clave = models.CharField(max_length=200, blank=True)
    abierta = models.BooleanField()
    habilitada = models.BooleanField(default=True)
    alumnos = models.ManyToManyField(
        User, related_name='alumnos', blank=True, null=True)
    docentes = models.ManyToManyField(
        User, related_name='docentes', blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.nombre


class Prueba(models.Model):

    ONLINE = 'online'
    ESCRITA = 'escrita'
    TIPOS_CHOICES = ((ONLINE, 'Online'), (ESCRITA, 'Escrita'))

    capacitacion = models.ForeignKey('Capacitacion')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    puntaje_total = models.IntegerField(blank=True, null=True)
    porcentaje_aprobacion = models.IntegerField()
    duracion = models.IntegerField()
    tipo = models.CharField(max_length=200, choices=TIPOS_CHOICES,
                            default=ONLINE)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    habilitada = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % self.nombre


class Categoria(models.Model):

    ALTERNATIVA = 'alternativa'
    VF = 'verdadero o falso'
    DESARROLLO = 'desarrollo'
    TIPOS_CHOICES = ((ALTERNATIVA, 'Alternativa'), (VF,
                     'Verdadero o Falso'), (DESARROLLO, 'Desarrollo'))

    prueba = models.ForeignKey('Prueba')
    nombre = models.CharField(max_length=200)
    minimo_preguntas = models.IntegerField(default=0)
    tipo = models.CharField(max_length=200, choices=TIPOS_CHOICES)

    def __unicode__(self):
        return u'%s' % self.nombre


class Pregunta(models.Model):

    categoria = models.ForeignKey('Categoria')
    pregunta = models.CharField(max_length=200)
    correcta = models.CharField(max_length=1, blank=True)
    puntaje = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.pregunta


class Alternativa(models.Model):

    pregunta = models.ForeignKey('Pregunta')
    alternativa = models.CharField(max_length=200)
    correcta = models.BooleanField()

    def __unicode__(self):
        return u'%s - %s' % (self.alternativa, self.pregunta)


class Calificacion(models.Model):

    APROBADO = 'aprobado'
    REPROBADO = 'reprobado'
    TIPOS_CHOICES = ((APROBADO, 'Aprobado'), (REPROBADO, 'Reprobado'))

    usuario = models.ForeignKey(User)
    prueba = models.ForeignKey('Prueba')
    fecha = models.DateField(default=datetime.date.today())
    hora_inicio = models.TimeField(default=datetime.datetime.now())
    hora_fin = models.TimeField(blank=True, null=True)
    terminada = models.BooleanField()
    puntaje = models.IntegerField(blank=True, null=True)
    porcentaje = models.IntegerField(blank=True, null=True)
    resultado = models.CharField(max_length=200, choices=TIPOS_CHOICES,
                                 blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.usuario, self.prueba)


class Respuesta(models.Model):

    calificacion = models.ForeignKey('Calificacion')
    pregunta = models.ForeignKey('Pregunta')
    alternativa = models.ForeignKey('Alternativa', blank=True,
                                    null=True)
    respuesta_vf = models.CharField(max_length=2, blank=True)
    respuesta_desarrollo = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.calificacion, self.pregunta)


class Archivo(models.Model):

    capacitacion = models.ForeignKey('Capacitacion')
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='archivos/%Y/%m/%d/%H/%M/%S/')

    def __unicode__(self):
        return u'%s' % self.nombre

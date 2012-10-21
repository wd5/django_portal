#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from elearning.models import Alternativa, Archivo, \
    Calificacion, Capacitacion, Categoria, Pregunta, Prueba, Respuesta, \
    UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Capacitacion)
admin.site.register(Prueba)
admin.site.register(Categoria)
admin.site.register(Pregunta)
admin.site.register(Alternativa)
admin.site.register(Calificacion)
admin.site.register(Respuesta)
admin.site.register(Archivo)

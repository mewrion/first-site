#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:06:48 2020

@author: mewrion
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name = 'post_list')
]


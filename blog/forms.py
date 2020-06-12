#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:49:24 2020

@author: mewrion
"""


from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields = ('title','text',)
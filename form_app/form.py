#coding:utf-8
from django import forms
from .models import *


class StuForm(forms.ModelForm):
    class Meta:
        model = student  # 基于模型的表单
        exclude = []  # uncomment this line and specify any field to exclude it from the form

class GradeForm(forms.ModelForm):
    class Meta:
        model = grade  # 基于模型的表单
        exclude = []  # uncomment this line and specify any field to exclude it from the form



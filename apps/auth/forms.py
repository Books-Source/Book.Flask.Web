#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    forms.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.24   15:47
-------------------------------------------------------------------------------
   @Change:   2020.05.24
-------------------------------------------------------------------------------
"""

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


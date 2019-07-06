# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.dentists import Dentists
from .api.dentist_info_did import DentistInfoDid


routes = [
    dict(resource=Dentists, urls=['/dentists'], endpoint='dentists'),
    dict(resource=DentistInfoDid, urls=['/dentist/info/<did>'], endpoint='dentist_info_did'),
]
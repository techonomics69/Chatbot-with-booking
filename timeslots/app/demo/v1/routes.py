# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.dentist_timeslots_did import DentistTimeslotsDid
from .api.dentist_did_timeslot_tid_cancel import DentistDidTimeslotTidCancel
from .api.dentist_did_timeslot_tid_reserve import DentistDidTimeslotTidReserve


routes = [
    dict(resource=DentistTimeslotsDid, urls=['/dentist/timeslots/<did>'], endpoint='dentist_timeslots_did'),
    dict(resource=DentistDidTimeslotTidCancel, urls=['/dentist/<did>/timeslot/<tid>/cancel'], endpoint='dentist_did_timeslot_tid_cancel'),
    dict(resource=DentistDidTimeslotTidReserve, urls=['/dentist/<did>/timeslot/<tid>/reserve'], endpoint='dentist_did_timeslot_tid_reserve'),
]
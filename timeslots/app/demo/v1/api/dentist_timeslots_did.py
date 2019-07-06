# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, Response

from . import Resource
from .. import schemas

from flask import jsonify
import json


class DentistTimeslotsDid(Resource):

    def get(self, did):

        token = request.args.get('token')

        if (token != None):
            with open('demo/data.json') as data_file:
                data = json.load(data_file)

            key = data.keys()

            dflag = 0

            availabletime = ""
            for item in key:
                if item == did:
                    dflag = 1
                    doctime = data[item]['availableTime']
                    for each in doctime:
                        availabletime += each + ", "
            availabletime = availabletime[:-2]


            if dflag == 1:
                return jsonify("A list of available timeslot of " + did + ": " + availabletime)
            else:
                return jsonify("Please correct the doctor name.")
        else:
            return Response("Please login to get further information.", status=401)



       
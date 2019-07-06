# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, Response

from . import Resource
from .. import schemas

from flask import jsonify
import requests
import json



class Dentists(Resource):

    def get(self):

        token = request.args.get('token')

        if (token != None):
            with open('demo/data.json') as data_file:
                data = json.load(data_file)

            file_out = open('demo/data.json', "w")

            file_out.write(json.dumps(data))
            data_file.close()
            file_out.close()

            result = ""
            originaldata = data.keys()
            for each in originaldata:
                if each == "availableDentist":
                    for time in data[each]:
                        result += time + ", "
            result = result[:-2]

            return jsonify("The available dentists: " + result)
        else:
            return Response("Please login to get further information.", status=401)




























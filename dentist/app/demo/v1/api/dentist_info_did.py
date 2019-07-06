# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, Response

from . import Resource
from .. import schemas

from flask import jsonify
import json


class DentistInfoDid(Resource):

    def get(self, did):

        token = request.args.get('token')
        if (token != None):
            with open('demo/data.json') as data_file:
                data = json.load(data_file)

            key = data.keys()

            info = {}
            flag = 0
            for item in key:
                if item == did:
                    flag = 1
                    docinfo = data[item]
                    info['name'] = item
                    info['location'] = docinfo['location']
                    info['specialization'] = docinfo['specialization']

            if flag == 1:
                return jsonify(info['name'] + " is located at " + info['location'] + " specializing in " + info['specialization'])
            else:
                return jsonify("The doctor you want to find does not exist")
        else:
            return Response("Please login to get further information.", status=401)






























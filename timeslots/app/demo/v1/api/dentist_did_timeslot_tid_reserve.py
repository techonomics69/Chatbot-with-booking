# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, Response

from . import Resource
from .. import schemas

from flask import jsonify

import json
from pprint import pprint


class DentistDidTimeslotTidReserve(Resource):

    def get(self, did, tid):

        token = request.args.get('token')

        if (token != None):
            with open('demo/data.json') as data_file:
                data = json.load(data_file)

            file_out = open('demo/data.json', "w")

            key = data.keys()
            numberofavailable = 0
            lenoftime = 0
            tflag = 0
            tflag1 = 0
            dflag = 0
            for item in key:
                if item == did:
                    dflag = 1

                    docinfo = data[item]

                    time = docinfo["time"]
                    lenoftime = len(time)
                    for each in time:
                        if each == tid and time[each] == "not reserved":
                            tflag = 1
                            time[each] = "reserved"
                            break;
                        if each == tid and time[each] == "reserved":
                            tflag1 = 2

            saveAvailableTime = ""
            for item in key:
                if item == did:
                    time = docinfo["time"]
                    for each in time:
                        if time[each] == "not reserved":
                            numberofavailable += 1
                            saveAvailableTime += each + ", "
            saveAvailableTime = saveAvailableTime[:-2]


            if numberofavailable < 1:
                docinfo['status'] = "not available"

            file_out.write(json.dumps(data))
            data_file.close()
            file_out.close()


            if tflag1 == 2 and dflag == 1 and len(saveAvailableTime) >= 1:
                return jsonify("The time " + tid + " you would like to book has been booked, and these are the time that you can book: " + saveAvailableTime)
            if tflag1 == 2 and dflag == 1 and len(saveAvailableTime) < 1:
                return jsonify("The time " + tid + " you would like to book has been booked, and there are no more available timeslot for " + did)
            if tflag == 1 and dflag == 1:
                return jsonify("You have successfully booked " + tid + " with " + did)
            if tflag == 0 and dflag == 1:
                return jsonify("We do not have time " + tid + " for "+ did)
            if tflag == 0 or dflag == 0:
                return jsonify("Please double check with the dentist and the timeslot")
        else:
            return Response("Please login to get further information.", status=401)




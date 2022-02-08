from time import sleep
from flask import Flask, jsonify, request, Response
from users import users

import os
from pathlib import Path

def init(app):
    @app.route('/', methods=['GET'])
    def ping():
        return jsonify({
            "response": "Hello World"
        })

    @app.route('/users', methods=['GET'])
    def users_handler():
        return jsonify({
            "users": users
        })

    @app.route('/loadfiles', methods=['POST'])
    def load_files():
        data = request.json
        # TODO: Create a library
        # Create .cfg & .dat files
        try:
            cfg_filename = "test.ext1"
            dat_filename = "test.ext2"
            # .cfg
            f = open(cfg_filename, "x") if os.path.isfile(cfg_filename) == False else open(cfg_filename, "w")
            f.write(data["cfg"])
            f.close()
            # .dat
            f = open(dat_filename, "x") if os.path.isfile(dat_filename) == False else open(dat_filename, "w")
            f.write(data["dat"])
            f.close()

            # Process files
            # .cfg
            sleep(1) # start simulation
            f = open(cfg_filename, "r")
            print(f.read())
            f.close()
            #.dat
            f = open(dat_filename, "r")
            print(f.read())
            f.close()
            sleep(1) # end simulation

            # Delete files
            os.remove(cfg_filename)
            os.remove(dat_filename)
            # os.remove()

            return Response(jsonify({
                "status": "ok"
            }).data, status=200, mimetype="application/json")
            
        except:
            return Response(jsonify({
                "status": "Error while creating creating/processing/removing files"
            }).data, status=500)


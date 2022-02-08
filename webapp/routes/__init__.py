from time import sleep
from flask import Flask, jsonify, request, Response
from users import users
from utils import CustomFile

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

    @app.route('/loadfiles', methods=['POST', 'GET'])
    def load_files():
        if request.method == "POST":
            data = request.json
            try:
                # Create .cfg & .dat files
                user = data["user"]
                cfg_filename = f"{user}_test.cfg"
                dat_filename = f"{user}_test.dat"
                cfg = CustomFile(cfg_filename)
                dat = CustomFile(dat_filename)
                # .cfg
                if not cfg.exists():
                    cfg.create()
                cfg.write(data["cfg"], overwrite=True)
                # .dat
                if not dat.exists():
                    dat.create()
                dat.write(data["dat"], overwrite=True)

                # Process files
                # .cfg
                print("CFG: ", cfg.read())
                #.dat
                print("DAT: ", dat.read())

                # Delete files
                cfg.remove()
                dat.remove()

                return Response(jsonify({
                    "status": "ok",
                    "message": "files created, processed and deleted"
                }).data, status=200, mimetype="application/json")
                
            except:
                return Response(jsonify({
                    "status": "Error while creating creating/processing/removing files"
                }).data, status=500)
        elif request.method == "GET":
            return "Try a POST request"


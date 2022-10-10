import sys, json, socket
from flask import render_template, request, make_response, url_for, Response
from flask_classful import FlaskView, route

class DevicesView(FlaskView):
    default_methods = ['GET', 'POST', 'PUT', 'DELETE']

    @route('/',methods=default_methods)
    def index(self):
        """Risposta ad una chiamata all'uri: http://127.0.0.1:8081/api/devices"""
        try:
            if request.method=="GET":
                msg = {"description":"L'URI ritorna tutti i dispositivi"}
                return Response(response=json.dumps(msg), status=200, headers=None, mimetype=None, content_type="application/json")
            elif request.method=="POST":
                msg = {"request_parameters":dict(request.form)}
                host = "127.0.0.1"
                port = 8081
                headers = {"location":f'http://{host}:{port}/api/devices'}
                return Response(response=json.dumps(msg), status=201, headers=headers, mimetype=None, content_type="application/json")
            else:
                msg = {"error": f'Metodo {request.method} non supportato'}
                return Response(response=json.dumps(msg), status=405, headers=None, mimetype=None, content_type="application/json")
        except Exception as e:
            print(e)
            msg={"error":str(e)}
            return Response(response=json.dumps(msg), status=500, headers=None, mimetype=None,
                            content_type="application/json")

    @route('/<id>',methods=default_methods)
    def device(self, id):
        """Risposta ad una chiamata all'uri: http://127.0.0.1:8081/api/devices/<id>"""
        try:
            if request.method=="GET":
                msg = {"description": f'Ho richiesto le informazioni del dispositivo con ID: {id}'}
                return Response(response=json.dumps(msg), status=200, headers=None, mimetype=None,
                                content_type="application/json")

            elif request.method=="PUT":
                msg = {"description": f'Ho richiesto la modifica delle informazioni del dispositivo con ID: {id}',
                       "request_parameters":dict(request.form)}
                return Response(response=json.dumps(msg), status=200, headers=None, mimetype=None,
                                content_type="application/json")

            elif request.method=="DELETE":
                msg = {"description": f'Ho richiesto la cancellazione delle informazioni del dispositivo con ID: {id}'}
                return Response(response=json.dumps(msg), status=200, headers=None, mimetype=None,
                                content_type="application/json")
            else:
                msg = {"error": f'Metodo {request.method} non supportato'}
                return Response(response=json.dumps(msg), status=405, headers=None, mimetype=None,
                                content_type="application/json")

        except Exception as e:
            msg = {"error": str(e)}
            return Response(response=json.dumps(msg), status=500, headers=None, mimetype=None,
                            content_type="application/json")


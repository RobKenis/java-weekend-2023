from flask import Flask, request
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.post("/")
def falco():
    app.logger.info("Falco alert received")
    app.logger.info(request.get_json())
    return "OK"

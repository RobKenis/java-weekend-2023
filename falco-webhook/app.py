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
    body = request.get_json()
    if body['priority'] == 'Warning' and body['rule'] == 'do_not_tcpdump':
        app.logger.info(f"TCPDUMP detected in [{body['output_fields']['k8s.pod.name']}] "
                        f"in namespace [{body['output_fields']['k8s.ns.name']}]")
    return "OK"

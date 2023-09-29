import logging

from flask import Flask, request
from kubernetes import client

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

v1 = client.CoreV1Api()


@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"


def _remove_allow_ingress_label(pod, namespace):
    app.logger.info(f"Removing label from pod [{pod}] in namespace [{namespace}]")
    v1.patch_namespaced_pod(pod, namespace, {"metadata": {"labels": {"allow-ingress-to": "none"}}})


@app.post("/")
def falco():
    app.logger.info("Falco alert received")
    body = request.get_json()
    if body['priority'] == 'Warning' and body['rule'] == 'do_not_tcpdump':
        app.logger.info(f"TCPDUMP detected in [{body['output_fields']['k8s.pod.name']}] "
                        f"in namespace [{body['output_fields']['k8s.ns.name']}]")
        _remove_allow_ingress_label(body['output_fields']['k8s.pod.name'],
                                    body['output_fields']['k8s.ns.name'])
    return "OK"

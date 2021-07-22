# Flask Function as a Service

[![Linkedin Badge](https://img.shields.io/badge/-Shivanjan%20Chakravorty-blue?style=plastic&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/shivanjan/)](https://www.linkedin.com/in/shivanjan/) [![Gmail Badge](https://img.shields.io/badge/-schakravorty846-c14438?style=plastic&logo=Gmail&logoColor=white&link=mailto:schakravorty846@gmail.com)](mailto:schakravorty846@gmail.com) [![Github Badge](https://img.shields.io/github/followers/Glitchfix?label=Glitchfix&logo=github&style=plastic)](https://github.com/Glitchfix)


## flask-faas

Migrating from serverless to a server application can be a headache at times.
flask-faas provides you a layer that sits on top of your existing serverless application handlers and helps them convert to Flask routes.
The prime goal is to be easy to use and easier to port. We currently support [Google Cloud Function](https://cloud.google.com/functions/), [AWS Lambda](https://aws.amazon.com/lambda/) and [OpenFaaS](https://www.openfaas.com/). We would have Azure Functions on the roadmap shortly.

## Installation

```py
pip install flask-faas
```

## Just import and use, no extra hassle!

```py
from flask_faas.gcp import google_cloud_function
from flask_faas.aws import aws_lambda
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/gcp/<arg0>",methods=["GET"])
@google_cloud_function
def my_cloud_function_handler(req):
    return jsonify(req.view_args)

@app.route("/aws/<arg0>/<arg1>",methods=["GET"])
@aws_lambda
def my_lambda_handler(event, context):
    return jsonify([event["pathParameters"]])

if __name__ == '__main__':
    app.run()
```

### Supported FaaS handler

- [x] Google Cloud Function
- [x] AWS Lambda
- [x] OpenFaaS

### TODO
- [ ] Azure Function


##### Resources: 
[Flask](https://flask.palletsprojects.com/)
[Google Cloud Function](https://cloud.google.com/functions/)
[AWS Lambda](https://aws.amazon.com/lambda/)
[OpenFaaS](https://www.openfaas.com/)

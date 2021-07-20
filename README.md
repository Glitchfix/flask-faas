# flask-serverless

[![Linkedin Badge](https://img.shields.io/badge/-Shivanjan%20Chakravorty-blue?style=plastic&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/shivanjan/)](https://www.linkedin.com/in/shivanjan/) [![Gmail Badge](https://img.shields.io/badge/-schakravorty846-c14438?style=plastic&logo=Gmail&logoColor=white&link=mailto:schakravorty846@gmail.com)](mailto:schakravorty846@gmail.com) [![Github Badge](https://img.shields.io/github/followers/Glitchfix?label=Glitchfix&logo=github&style=plastic)](https://github.com/Glitchfix)

Decorators for converting your existing serverless handlers to Flask.
A valid use case would be porting your application from FaaS to a CaaS form factor.

## Just import and use, no extra hassle!

```py
from flask_serverless.gcp import google_cloud_function
from flask_serverless.aws import aws_lambda
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

### Supported serverless handler

- [x] Google Cloud Function
- [x] AWS Lambda
- [ ] Azure Function (TODO)
- [x] OpenFaaS



##### Resources: 
[Flask](https://flask.palletsprojects.com/)
[Google Cloud Function](https://cloud.google.com/functions/)
[AWS Lambda](https://aws.amazon.com/lambda/)
[OpenFaaS](https://www.openfaas.com/)

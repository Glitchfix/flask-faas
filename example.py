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
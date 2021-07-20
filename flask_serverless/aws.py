import time
from functools import wraps
from flask import request, current_app


class LambdaContext():

    function_name = ""
    function_version = ""
    invoked_function_arn = ""
    memory_limit_in_mb = float("inf")
    aws_request_id = ""
    log_group_name = ""
    log_stream_name = ""

    request_start_time = 0
    time_remaining = 0

    def get_remaining_time_in_millis(self):
        return (current_app.config['PERMANENT_SESSION_LIFETIME'] - (time.time() - self.request_start_time) * 1000)

    def __init__(self, function_name):
        self.request_start_time = time.time()
        self.function_name = function_name


def aws_lambda(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        event = {
            "resource": "/",
            "path": request.path,
            "httpMethod": request.method,
            "requestContext": {
                "resourcePath": request.url_root,
                "httpMethod": request.method,
                "path": request.path,

            },
            "headers": request.headers,
            "multiValueHeaders": request.headers,
            "queryStringParameters": request.values,
            "multiValueQueryStringParameters": request.values,
            "pathParameters": request.view_args,
            "stageVariables": None,
            "body": request.get_data(),
            "isBase64Encoded": False,
        }
        context = LambdaContext(function_name=current_app.name)
        return f(event, context)

    return decorator

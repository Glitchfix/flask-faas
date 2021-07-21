from functools import wraps
from flask import request

def google_cloud_function(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        req = request
        req.args = args
        req.kwargs = kwargs
        return f(req)
    
    return decorator
from flask import jsonify, request
from functools import wraps
from importlib import import_module
from validator import validate as _validate


# Decorators

def validate(rules: dict):
    """Validate request data."""

    def decorator(view_func):
        def wrapped_view(*args, **kwargs):
            # 取決於前端發送資料格式
            result, data, _ = _validate(request.json, rules, True)
            # result, data, _ = _validate(request.values.to_dict(), rules, True)

            if result:
                kwargs['data'] = data
                return view_func(*args, **kwargs)

            return response('', status = 422)

        return wraps(view_func)(wrapped_view)

    return decorator


# Import module

def import_attribute(path: str):
    pkg, attr = path.rsplit('.', 1)
    return getattr(import_module(pkg), attr)


# Ip

def ip2int(ip: str):
    """Convert string ip to int."""

    int_ip = 0
    for i in ip.split('.'):
        int_ip = int_ip << 8 | int(i)
    return int_ip


def int2ip(int_ip: int):
    """Convert int ip to string."""

    ip = []

    for _ in range(4):
        ip.append(str(int_ip & 255))
        int_ip >>= 8

    return '.'.join(ip[::-1])


# Request

def get_request_ip():
    return request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)


# Response

def response(message = 'success', code = 0, status = 200):
    """Return response with code and message (json).

    Defaults params :
        message : str = 'success'
        code : int = 0
        status: int = 200

    Example return json : {
        "code": code,
        "message": message
    }
    """

    return jsonify({
        'code': code,
        'message': message
    }), status

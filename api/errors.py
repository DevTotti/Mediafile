from flask import Response, jsonify

def invalid_request() -> Response :
    output = {"error":
                {'message':'40 error: Invalid Request'}
                }

    response = jsonify({'result': output})
    response.status_code = 400
    return response

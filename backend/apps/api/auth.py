from rest_framework_jwt.authentication import JSONWebTokenAuthentication


def authenticate(request):
    auth_tuple = JSONWebTokenAuthentication().authenticate(request)
    if auth_tuple is not None:
        user, jwt_value = auth_tuple
        return user
    return None

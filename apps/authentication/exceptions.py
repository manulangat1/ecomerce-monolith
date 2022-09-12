from rest_framework.exceptions import APIException 


class ProfileNotFound(APIException):
    default_detail = "Profile not found"
    default_code = 404
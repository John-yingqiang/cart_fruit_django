from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.utils import six
from rest_framework.serializers import Serializer
from collections import OrderedDict

class JsonResponse(Response):
    def __init__(self, data=None, code=None, 
                        desc=None, status=None, 
                        template_name=None,
                        headers=None, exception=False, content_type=None):
        super(Response, self).__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                    'You passed a Serializer isinstance as data, but probably'
                     'meant to pass serialized .data or .error'
                    )
            raise AssertionError(msg)
        
        if isinstance(data, list):            
            self.data = {'code':code, 'desc':desc, 'data':{'count':len(data), 'detail':data}}
        elif not data:
            self.data = {'code':code, 'desc':desc, 'data':{'count':0, 'detail':data}}
        else:
            self.data = {'code':code, 'desc':desc, 'data':{'count':1, 'detail':data}}
            
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        response.data['code'] = response.status_code
        response.data['desc'] = response.data['detail']
        response.data['data'] = None

    return response

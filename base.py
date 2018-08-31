import requests
from settings import ACCESS_TOKEN

API_VERSION = '5.52'
API_HOST = 'https://api.vk.com'
API_METHOD_ENDPOINT = API_HOST + '/method'

METHOD_WALL_GET = 'wall.get'


class VKAPI:
    
    def __init__(self, token=ACCESS_TOKEN, id=None, requests_lib=requests):
        self.token = token
        self.id = id
        self.requests = requests_lib

    def _get_mandatory_params(self):
        return {'access_token': self.token, 'version': API_VERSION}
    
    def _get_method_endpoint(self, method):
        return '/'.join([API_METHOD_ENDPOINT, method])
    
    def query(self, method, **params):
        all_params = dict(self._get_mandatory_params(), **params)
        querystring = '?' + "&".join("{param}={value}".format(param=p, value=v) for p, v in all_params.items() if v is not None)
        url = self._get_method_endpoint(method) +  querystring
        return self.requests.get(url).content
    
    def wall_get(self, owner_id=None, domain=None, offset=None, count=None, filter='all', extended=0, fields=None):
        return self.query(METHOD_WALL_GET, owner_id=owner_id or self.id, domain=domain, offset=offset, count=count, filter=filter, extended=extended, fields=fields)

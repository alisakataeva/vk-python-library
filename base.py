import requests

try:
    from .local import ACCESS_TOKEN
except ImportError:
    print('Define ACCESS_TOKEN in local.py')

class VKAPI:
    
    def __init__(self, id=None):
        self.server = 'https://api.vk.com/method'
        self.token = ACCESS_TOKEN
        self.id = id
        self.version = '5.52'
        
    def query(self, model, params=None):
        if params:
            paramstr = ''
            for key, value in params.items():
                paramstr += ('&' + key + '=' + value)
            query = self.server + '/' + model + '?v=&access_token=' + paramstr
            query = '%s/%s?v=%s&access_token=%s%s' % (self.server, model, self.version, self.token, paramstr)
        else:
            query = '%s/%s?v=%s&access_token=%s' % (self.server, model, self.version, self.token)
        return query
    
    def get_wall_posts(self, owner_id=None):
        if owner_id:
            return requests.get(self.query('wall.get', {'owner_id': owner_id})).content
        else:
            return requests.get(self.query('wall.get')).content

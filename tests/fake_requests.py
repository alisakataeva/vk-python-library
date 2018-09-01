from urllib.parse import urlparse
from base import METHOD_WALL_GET

class FakeResponse:
    def __init__(self, content=None):
        self.content = content
    

class FakeRequests:
    def get(self, url):
        parts = urlparse(url)
        querystring = parts.query.split('&')
        method = parts.path.split('/')[-1]
        if method == METHOD_WALL_GET:
            return FakeResponse({
                "response": {
                    "count": 1067,
                    "items": []
                }
            })


requests = FakeRequests()
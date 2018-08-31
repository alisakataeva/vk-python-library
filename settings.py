ACCESS_TOKEN = 'PUT_YOUR_TOKEN_HERE'

try:
    from local import ACCESS_TOKEN
except ImportError:
    print('Define ACCESS_TOKEN in local.py')
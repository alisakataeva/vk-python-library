import unittest
from base import VKAPI
from tests.fake_requests import requests

class TestVkApiMethods(unittest.TestCase):

    def setUp(self):
        self.vk = VKAPI(requests_lib=requests)

    def test_wall_get(self):
        result = self.vk.wall_get(owner_id='10011')
        self.assertDictEqual(result, {
                "response": {
                    "count": 1067,
                    "items": []
                }
            }, 'wrong result')

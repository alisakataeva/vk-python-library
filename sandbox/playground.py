from base import VKAPI

def get_all_posts_by_id(id=None):
    vk_api = VKAPI()
    print(vk_api.get_wall_posts(id))
from classes.posts_dao import PostsDAO
from classes.posts import Posts

import pytest

path = '../data/data.json'


class PostsTest:
    def test_get_post_by_user(self):
        post = PostsDAO(path)
        user_posts = post.get_posts_by_user('leo')
        assert len(user_posts) == 2, 'Ошибка в получении постов'



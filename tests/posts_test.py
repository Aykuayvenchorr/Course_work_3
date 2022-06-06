from classes.posts_dao import PostsDAO
from classes.posts import Posts

import pytest

path = '../data/data.json'


class TestPosts:
    def test_get_post_by_user(self):
        post = PostsDAO(path)
        user_posts = post.get_posts_by_user('leo')
        assert len(user_posts) == 2, 'Ошибка в получении постов'

    def test_get_comments_by_post_id(self):
        post = PostsDAO(path)
        comments = post.get_comments_by_post_id(1)
        assert len(comments) == 4, 'Ошибка в получении комментариев'

    # def test_search_for_post(self):
    #     post = PostsDAO(path)
    #     result = post.search_for_posts('закат')
    #     assert



from classes.posts_dao import PostsDAO
from classes.posts import Posts
import json
import os

import pytest

# project_path = os.getcwd()
#
# file_path = "\\data\\data.json"

# path_post = '../data/data.json'
#
path_comm = '../data/comments.json'


class TestPostsDAO:

    @pytest.fixture()
    def post_dao(self):
        post_dao_instance = PostsDAO('./mock_posts')
        return post_dao_instance

# Функция получения всех постов

    def test_get_posts_all_types(self, post_dao):
        posts = post_dao.get_posts_all()

        assert type(posts) == list, 'Incorrect type for result'

        assert type(posts[0]) == Posts, 'Incorrect type for single item'

    def test_get_all_fiels(self, post_dao):
        posts = post_dao.get_posts_all()
        post = posts[0]

        fields = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']

        for field in fields:
            assert hasattr(post, field), f'Нет поля {field}'

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_posts_all()
        correct_pks = {1, 2, 3, 4, 5, 6, 7, 8}

        pks = set([post.pk for post in posts])
        assert pks == correct_pks, 'Не совпадают полученные id'

# Функция

    def test_get_post_by_user(self, post_dao):
        user_posts = post_dao.get_posts_by_user('leo')
        assert len(user_posts) == 2, 'Ошибка в получении постов'

    def test_get_comments_by_post_id(self, post_dao):
        comments_user = post_dao.get_comments_by_post_id(1, path_comm)
        assert len(comments_user) == 4, 'Ошибка в получении комментариев'

    def test_search_for_post(self, post_dao):
        result = post_dao.search_for_posts('закат')
        for res in result:
            assert res.poster_name == 'hank', 'Ошибка в поиске постов'



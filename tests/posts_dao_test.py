from classes.posts_dao import PostsDAO
from classes.posts import Posts

import pytest


def check_fields(post):
    """Проверяет наличие ключей"""
    fields = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']

    for field in fields:
        assert hasattr(post, field), f'Нет поля {field}'


class TestPostsDAO:

    @pytest.fixture()
    def post_dao(self):
        post_dao_instance = PostsDAO('tests/mock_posts')
        return post_dao_instance

    # Функция получения всех постов

    def test_get_posts_all_types(self, post_dao):
        posts = post_dao.get_posts_all()

        assert type(posts) == list, 'Incorrect type for result'

        assert type(posts[0]) == Posts, 'Incorrect type for single item'

    def test_get_all_fiels(self, post_dao):
        posts = post_dao.get_posts_all()
        post = posts[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_posts_all()
        correct_pks = {1, 2, 3, 4, 5, 6, 7, 8}

        pks = set([post.pk for post in posts])
        assert pks == correct_pks, 'Не совпадают полученные id'

    # Функция получения постов по имени автора

    def test_get_post_by_user(self, post_dao):
        user_posts = post_dao.get_posts_by_user('leo')
        assert len(user_posts) == 2, 'Ошибка в получении постов'
        assert type(user_posts) == list, 'Incorrect type for result'

        for post in user_posts:
            assert post.poster_name == 'leo', 'Ошибка в поиске по имени'
            assert type(post) == Posts, 'Incorrect type for result single item'

    def test_get_by_user_fields(self, post_dao):
        posts = post_dao.get_posts_by_user('leo')
        for post in posts:
            check_fields(post)

    # Функция получения постов по вхождению строки

    def test_search_for_post(self, post_dao):
        result = post_dao.search_for_posts('закат')
        assert type(result) == list, 'Incorrect type for result'
        for res in result:
            assert res.poster_name == 'hank', 'Ошибка в поиске постов'
            assert type(res) == Posts, 'Incorrect type for result single item'

    def test_search_in_content_not_found(self, post_dao):
        posts = post_dao.search_for_posts('такого слова точно нет')
        assert posts == [], 'Should be [] for not existent substring'

    @pytest.mark.parametrize('s, expected_pks', [('Ага', {1})])
    def test_search_in_content_results(self, post_dao, s, expected_pks):
        posts = post_dao.search_for_posts(s)
        pks = set([post.pk for post in posts])
        assert expected_pks == pks, f'Incorrect result searching for {s}'

    # Функция получения одного поста по pk

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        assert type(post) == Posts, 'Incorrect type for result single item'

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_post_by_pk(999)
        assert post is None, 'Should be None for non existent pk'

    @pytest.mark.parametrize('pk', [1, 2, 3, 4, 5, 6, 7, 8])
    def test_get_post_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_post_by_pk(pk)
        assert post.pk == pk, f'Incorrect pk for requested post with pk == {pk}'

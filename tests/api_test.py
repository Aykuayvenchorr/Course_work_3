import pytest

from run import app


class TestApi:

    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

    @pytest.fixture
    def app_instance(self):
        return app.test_client()

    def test_all_posts_have_correct_status_code(self, app_instance):
        result = app_instance.get("/api/posts/", follow_redirects=True)
        assert result.status_code == 200

    def test_all_posts_have_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/", follow_redirects=True)
        list_of_posts = result.get_json()

        for post in list_of_posts:
            assert post.keys() == self.post_keys, 'Неправильные ключи у словаря'

    def test_single_post_has_correct_status_code(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200

    def test_single_post_has_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        post = result.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.post_keys
        



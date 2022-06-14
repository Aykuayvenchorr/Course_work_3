import json
from classes.posts import Posts
from exceptions import DataSourceBrokenError


class PostsDAO:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
        """Загружаем все посты из JSON и превращаем их в объект класса Posts (служебная функция)"""
        try:
            with open(self.path, encoding='utf-8') as file:
                posts_data = json.load(file)
                posts = []
                for post in posts_data:
                    posts.append(Posts(post['pk'],
                                       post['poster_name'],
                                       post['poster_avatar'],
                                       post['pic'],
                                       post['content'],
                                       post['views_count'],
                                       post['likes_count']
                                       ))
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataSourceBrokenError("Файл с данными поврежден")
        else:
            return posts

    def get_posts_all(self):
        """Получаем все посты (пользовательская функция)"""
        return self.load_posts()

    def get_posts_by_user(self, user_name):
        """Поиск постов по имени пользователя"""
        posts = self.get_posts_all()
        user_post = []
        names = []
        for post in posts:
            names.append(post.poster_name)
            if user_name == post.poster_name:
                user_post.append(post)
        if user_name not in names:
            raise ValueError('Такого пользователя нет')
        return user_post

    def search_for_posts(self, query):
        """Поиск постов по вхождению слов"""
        output_data = []
        for post in self.load_posts():
            if query in post.content:
                output_data.append(post)
        return output_data

    def get_post_by_pk(self, pk):
        """Поиск постов по pk"""
        posts = self.get_posts_all()
        for post in posts:
            if pk == post.pk:
                return post


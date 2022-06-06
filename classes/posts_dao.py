import json
from classes.posts import Posts
from exceptions import DataSourceBrokenError


class PostsDAO:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
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
        return self.load_posts()

    def get_posts_by_user(self, user_name):
        posts = self.get_posts_all()
        user_post = []
        names = []
        for post in posts:
            names.append(post['poster_name'])
            if user_name == post['poster_name']:
                user_post.append(post)
        if user_name not in names:
            raise ValueError('Такого пользователя нет')  # maybe error
        return user_post

    def get_comments_all(self, path='../data/comments.json'):
        with open(path, encoding='utf-8') as file:
            comments_data = json.load(file)
            return comments_data

    def get_comments_by_post_id(self, post_id):
        comments = self.get_comments_all()  # maybe error
        user_comments = []
        list_id = []
        for comment in comments:
            list_id.append(comment['post_id'])
            if post_id == comment['post_id']:
                user_comments.append(comment)
        if post_id not in list_id:
            raise ValueError('Такого поста нет')
        return user_comments

    def search_for_posts(self, query):
        output_data = []
        for post in self.load_posts():
            if query in post["content"]:
                output_data.append(post)
        return output_data

    def get_post_by_pk(self, pk):
        posts = self.get_posts_all()
        for post in posts:
            if pk == post['pk']:
                return post

#
# post_ex = PostsDAO('../data/data.json')
# print(post_ex.get_posts_by_user('leo'))
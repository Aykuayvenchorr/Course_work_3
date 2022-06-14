import json

from classes.comments import Comments
from exceptions import DataSourceBrokenError


class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def load_comments(self):
        """Загрузка комментариев из JSON"""
        try:
            with open(self.path, encoding='utf-8') as file:
                comments_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataSourceBrokenError("Файл с данными поврежден")
        else:
            return comments_data

    def get_comments_all(self):
        """Преобразование комментариев в объект класса Comments"""
        comments = self.load_comments()
        list_of_comments = [Comments(**comment) for comment in comments]
        return list_of_comments

    def get_comments_by_post_id(self, post_id):
        """Получение комментариев по id"""
        comments = self.get_comments_all()
        user_comments = []
        list_id = []
        for comment in comments:
            list_id.append(comment.post_id)
            if post_id == comment.post_id:
                user_comments.append(comment)
        if post_id not in list_id:
            raise ValueError('Такого поста нет')
        else:
            return user_comments



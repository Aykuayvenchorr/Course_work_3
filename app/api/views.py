import logging

from flask import Blueprint, jsonify

from classes.comments_dao import CommentsDAO
from classes.posts_dao import PostsDAO
from config import DATA_PATH_POST, DATA_PATH_COMMENTS

bp_api = Blueprint("bp_api", __name__)

post_main = PostsDAO(DATA_PATH_POST)
comments_dao = CommentsDAO(DATA_PATH_COMMENTS)

api_logger = logging.getLogger("api_logger")


@bp_api.route('/')
def api_posts_hello():
    return 'Это api. Доступные эндпоинты /api/posts/ и /api/posts/<pk>.'


@bp_api.route('/posts/')
def api_posts_all():
    all_posts = post_main.get_posts_all()
    api_logger.debug("Запрошены все посты")
    return jsonify([post.as_dict() for post in all_posts])


@bp_api.route('/posts/<int:pk>')
def api_posts_single(pk):
    post = post_main.get_post_by_pk(pk)
    api_logger.debug(f"Запрошен пост {pk}")
    return jsonify(post.as_dict())


from flask import Blueprint, render_template, request
from classes.posts_dao import PostsDAO
import os

main_blueprint = Blueprint('main_blueprint', __name__)
file_path = "\\data\\data.json"
project_path = os.getcwd()
path_post = project_path + file_path


@main_blueprint.route('/')
def main_page():
    post_main = PostsDAO(path_post)
    posts = post_main.get_posts_all()
    return render_template('index.html', posts=posts)




from flask import Blueprint, render_template, request, abort, redirect

from classes.comments_dao import CommentsDAO
from classes.posts_dao import PostsDAO
import os
from config import DATA_PATH_POST, DATA_PATH_COMMENTS, DATA_PATH_BOOKMARKS

posts_blueprint = Blueprint('posts_blueprint', __name__)
post_main = PostsDAO(DATA_PATH_POST)
comments_dao = CommentsDAO(DATA_PATH_COMMENTS)


@posts_blueprint.route('/')
def main_page():
    posts = post_main.get_posts_all()
    return render_template('index.html', posts=posts)


@posts_blueprint.route('/posts/<int:pk>/')
def single_post_page(pk):
    post = post_main.get_post_by_pk(pk)
    if post is None:
        abort(404)
    comments = comments_dao.get_comments_by_post_id(pk)
    text = post.content.split(' ')
    for count, word in enumerate(text):
        if word.startswith('#'):
            text[count] = f'<a href="/tag/{word[1:]}">{word}</a>'
    text_tags = ' '.join(text)
    return render_template('post.html', post=post, comments=comments, text_tags=text_tags)


@posts_blueprint.route('/users/<user_name>/')
def post_by_user_page(user_name):
    posts = post_main.get_posts_by_user(user_name)
    if not posts:
        abort(404, 'Такого пользователя не существует')
    return render_template('user-feed.html', posts=posts, user_name=user_name)


@posts_blueprint.route('/search/')
def posts_search_page():
    query = request.args.get("s", "")
    if query == '':
        posts = []
    else:
        posts = post_main.search_for_posts(query)
    return render_template('search.html', posts=posts, query=query)


@posts_blueprint.route('/tag/<tagname>')
def posts_with_tags(tagname):
    posts = post_main.get_posts_all()
    new_posts = []
    tag = '#' + tagname
    for post in posts:
        if tag in post.content:
            new_posts.append(post)
    return render_template('tag.html', new_posts=new_posts, tagname=tagname)


@posts_blueprint.route('/bookmarks/add/<post_id>')
def add_bookmarks(post_id):
    posts = post_main.get_posts_all()
    for post in posts:
        if post.pk == post_id:
            with open('../../data/bookmarks.json', 'w') as file:
                file.write(post)
    return redirect('/', code=302)




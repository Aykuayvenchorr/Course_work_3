from flask import Blueprint, render_template, request
from classes.posts_dao import Posts

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def main_page():

    return render_template('index.html')


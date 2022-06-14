from flask import Flask, send_from_directory

from app.api.views import bp_api
from app.posts.views import posts_blueprint
from exceptions import DataSourceBrokenError
import logger


def create_and_config_app(config_path):
    app = Flask(__name__)

    app.config['JSON_AS_ASCII'] = False
    app.config.from_pyfile(config_path)
    app.register_blueprint(posts_blueprint)
    app.register_blueprint(bp_api, url_prefix='/api')

    logger.config()

    return app


app = create_and_config_app('config.py')



@app.errorhandler(404)
def page_error_404(error):
    return f'Такой страницы нет {error}', 404


@app.errorhandler(500)
def page_error_500(error):
    return f'На сервере произошла ошибка - {error}', 500


@app.errorhandler(DataSourceBrokenError)
def page_error_data_source_broken(error):
    return f'Ошибка, на сайте поломались данные {error}', 500


@app.errorhandler(ValueError)
def page_error_value(error):
    return f'{error}', 500


if __name__ == "__main__":
    app.run(debug=True)

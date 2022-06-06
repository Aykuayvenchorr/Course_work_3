from flask import Flask, send_from_directory

from app.main.views import main_blueprint


app = Flask(__name__)
app.config['PATH'] = 'data/data.json'

app.register_blueprint(main_blueprint)


if __name__ == "__main__":
    app.run(debug=True)

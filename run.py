from app.api_flask.api_flask import ApiFlask
from app.api_flask.utils import register_blueprints

app = ApiFlask(__name__)
register_blueprints(app, root='app.views')

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

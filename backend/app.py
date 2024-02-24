import os
import logging

from flask import Flask
from routes.main_routes import main_bp


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..','frontend', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, '..', 'frontend', 'static')

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = os.getenv("FLASK_SECRET_KEY")  # Set a secret key for flashing messages, replace with your own secret key


# Register routes
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

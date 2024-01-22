import os
from flask import Flask, render_template

# template_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),'frontend/templates')
template_dir = 'frontend/templates'
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

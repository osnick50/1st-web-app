import os
from flask import Flask, render_template, jsonify

# template_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),'frontend/templates')
template_dir = 'frontend/templates'
app = Flask(__name__, template_folder=template_dir)

JOBS = [
    {
        'id': 1,
        'title': "Software Engineer",
        'location': "Wrocław",
        'salary': "1500$"
    },
    {
        'id': 2,
        'title': "ML Intern",
        'location': "Warsaw",
        'salary': "1000$"
    },
    {
        'id': 3,
        'title': "Frontend Developer",
        'location': "Remote"
    },
    {
        'id': 4 ,
        'title': "Data Scientist",
        'location': "Gdańsk",
        'salary': "2500$"
    },
]

@app.route("/")
def home_page():
    return render_template('home.html', jobs=JOBS, company_name="Best Jobs")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)    
    

if __name__ == '__main__':
    app.run(debug=True)

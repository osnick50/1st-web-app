import os
from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

# template_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),'frontend/templates')
template_dir = 'frontend/templates'
app = Flask(__name__, template_folder=template_dir)

def load_jobs_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs_list = []
        for dict_row in result.mappings():
            jobs_list.append(dict(dict_row))
        return jobs_list

@app.route("/")
def home_page():
    jobs = load_jobs_db()
    return render_template('home.html', jobs=jobs, company_name="Best Jobs")

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_db()
    return jsonify(jobs)    
    

if __name__ == '__main__':
    app.run(debug=True)

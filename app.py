import os
from dotenv import load_dotenv
import logging
from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

load_dotenv()

# template_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),'frontend/templates')
template_dir = 'frontend/templates'
app = Flask(__name__, template_folder=template_dir)

logging.basicConfig(level=logging.INFO)

def load_jobs_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs"))
            jobs_list = []
            for dict_row in result.mappings():
                jobs_list.append(dict(dict_row))
            logging.info("Jobs loaded from DB")
            return jobs_list
    except Exception as e:
        logging.info("Error occured while loading jobs from DB: ", e)

@app.route("/")
def home_page():
    try:
        jobs = load_jobs_db()
        logging.info("Jobs info loaded ")
        return render_template('home.html', jobs=jobs, company_name="Best Jobs")
    except Exception as e:
        logging.info("Error while jobs loading: ", e)



@app.route("/api/jobs")
def list_jobs():
    try:
        jobs = load_jobs_db()
        logging.info("Jobs info loaded")
        return jsonify(jobs)
    except Exception as e:
        logging.info("Error while jobs loading: ", e) 
    

if __name__ == '__main__':
    app.run(debug=True)

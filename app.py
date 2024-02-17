import logging
from flask import Flask, render_template, jsonify
from database import load_jobs_db, load_job_db

# template_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),'frontend/templates')
template_dir = 'frontend/templates'
app = Flask(__name__, template_folder=template_dir)

logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def home_page():
    try:
        jobs = load_jobs_db()
        logging.info("Jobs info loaded on page")
        return render_template('home.html', jobs=jobs)
    except Exception as e:
        logging.error("Error while jobs loading: ", e)


@app.route("/job/<id>")
def show_job(id):
     try:
        job = load_job_db(id)
        if not job:
            return "Not found", 404
        return render_template('jobpage.html', job=job)
     except Exception as e:
        logging.error("Error while jobs loading: ", e) 


@app.route("/api/jobs")
def list_jobs():
    try:
        jobs = load_jobs_db()
        logging.info("Jobs info loaded")
        return jsonify(jobs)
    except Exception as e:
        logging.error("Error while jobs loading: ", e) 


@app.route("/api/health")
def health_check():
        return jsonify({'status': 'ok'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

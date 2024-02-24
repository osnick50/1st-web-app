import os
import logging
from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from database import load_jobs_from_db, load_job_id, add_application_to_db

TEMPLATE_DIR = 'frontend/templates'
app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.secret_key = os.getenv("FLASK_SECRET_KEY")  # Set a secret key for flashing messages, replace with your own secret key

logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def home_page():
    try:
        jobs = load_jobs_from_db()
        logging.info("Jobs info loaded on page")
        return render_template('home.html', jobs=jobs)
    except Exception as e:
        logging.error("Error while jobs loading: ", e)


@app.route("/job/<id>")
def show_job(id):
    try:
        job = load_job_id(id)
        if not job:
            return "Not found", 404
        return render_template('jobpage.html', job=job)
    except Exception as e:
        logging.error("Error while jobs loading: ", e) 


@app.route("/job/<id>/apply",  methods=["post"])
def apply_to_job(id):
    try:
        data = request.form
        response = add_application_to_db(id, data)
        if response:
            flash('Application submitted successfully!', 'success')
            return redirect(url_for('show_job', id=id))  # Redirect to /job/1 instead of rendering jobpage.html
        else:
            flash('Error occurred during job application', 'error')
            return redirect(url_for('show_job', id=id))
    except Exception as e:
        logging.error(f"Apply error: {e}")
        flash('Error occurred during job application', 'error')
        return redirect(url_for('show_job', id=id))

@app.route("/api/jobs")
def list_jobs():
    try:
        jobs = load_jobs_from_db()
        logging.info("Jobs info loaded")
        return jsonify(jobs)
    except Exception as e:
        logging.error("Error while jobs loading: ", e) 


@app.route("/api/health")
def health_check():
        return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

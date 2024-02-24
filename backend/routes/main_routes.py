import os
import logging
from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from services.database import load_jobs_from_db, load_job_id, add_application_to_db

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home_page():
    try:
        jobs = load_jobs_from_db()
        logging.info("Jobs info loaded on page")
        return render_template('home.html', jobs=jobs)
    except Exception as e:
        logging.error("Error while jobs loading: ", e)


@main_bp.route("/job/<id>")
def show_job(id):
    try:
        job = load_job_id(id)
        if not job:
            return "Not found", 404
        return render_template('jobpage.html', job=job)
    except Exception as e:
        logging.error("Error while jobs loading: ", e) 


@main_bp.route("/job/<id>/apply",  methods=["post"])
def apply_to_job(id):
    try:
        data = request.form
        response = add_application_to_db(id, data)
        if response:
            flash('Application submitted successfully!', 'success')
            return redirect(url_for('main.show_job', id=id))  # Redirect to /job/1 instead of rendering jobpage.html
        else:
            flash('Error occurred during job application', 'error')
            return redirect(url_for('main.show_job', id=id))
    except Exception as e:
        logging.error(f"Apply error: {e}")
        flash('Error occurred during job application', 'error')
        return redirect(url_for('main.show_job', id=id))


@main_bp.route("/api/jobs")
def list_jobs():
    try:
        jobs = load_jobs_from_db()
        logging.info("Jobs info loaded")
        return jsonify(jobs)
    except Exception as e:
        logging.error("Error while jobs loading: ", e) 


@main_bp.route("/api/health")
def health_check():
        return jsonify({'status': 'ok'})
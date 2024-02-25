import logging
from flask import Blueprint, jsonify
from services.database import load_jobs_from_db

api_bp = Blueprint('api', __name__)

@api_bp.route("/api/jobs")
def list_jobs():
    try:
        jobs = load_jobs_from_db()
        logging.info("Jobs info loaded")
        return jsonify(jobs)
    except Exception as e:
        logging.error("Error while jobs loading: ", e) 


@api_bp.route("/api/health")
def health_check():
        return jsonify({'status': 'ok'})
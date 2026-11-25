
from flask import Blueprint, request, jsonify, current_app
from services.file_handler import save_image, save_video
from services.cleanup import cleanup_old_files
import uuid

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/jobs", methods=["POST"])
def create_job():

    cleanup_old_files(
        [
            current_app.config["FACE_FOLDER"],
            current_app.config["VIDEO_FOLDER"],
            current_app.config["OUTPUT_FOLDER"]
        ],
        current_app.config["FILE_RETENTION_SECONDS"]
    )

    if request.form.get("consent") != "yes":
        return jsonify({
            "error": "Permission confirmation is required."
        }), 400

    face = request.files.get("face")
    video = request.files.get("video")

    if not face or not video:
        return jsonify({
            "error": "Both files are required."
        }), 400

    try:
        face_name = save_image(
            face,
            current_app.config["FACE_FOLDER"],
            current_app.config["ALLOWED_IMAGES"]
        )

        video_name = save_video(
            video,
            current_app.config["VIDEO_FOLDER"],
            current_app.config["ALLOWED_VIDEOS"]
        )

    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    except Exception:
        return jsonify({
            "error": "Upload failed. Please try again."
        }), 500

    job_id = uuid.uuid4().hex

    return jsonify({
        "success": True,
        "job_id": job_id,
        "status": "waiting_for_ai_engine",
        "message": "Files uploaded. AI processing is not connected yet.",
        "files": {
            "face": face_name,
            "video": video_name
        }
    }), 202


@api.route("/health", methods=["GET"])
def health():
    return jsonify({
        "success": True,
        "message": "AI Face Studio API is running."
    })

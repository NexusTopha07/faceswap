
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY", "change-this-before-deployment"
    )

    MAX_CONTENT_LENGTH = 110 * 1024 * 1024

    FACE_FOLDER = os.path.join(BASE_DIR, "uploads", "faces")
    VIDEO_FOLDER = os.path.join(BASE_DIR, "uploads", "videos")
    OUTPUT_FOLDER = os.path.join(BASE_DIR, "uploads", "outputs")

    ALLOWED_IMAGES = {"jpg", "jpeg", "png", "webp"}
    ALLOWED_VIDEOS = {"mp4", "webm", "mov"}

    FILE_RETENTION_SECONDS = 3600

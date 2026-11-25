
import os
import uuid
from werkzeug.utils import secure_filename
from PIL import Image

def get_extension(filename):
    if "." not in filename:
        return ""

    return filename.rsplit(".", 1)[1].lower()


def save_image(file, folder, allowed):
    extension = get_extension(file.filename)

    if extension not in allowed:
        raise ValueError("Unsupported image format.")

    try:
        image = Image.open(file.stream)
        image.verify()
    except Exception:
        raise ValueError("Invalid image file.")

    file.stream.seek(0)

    name = uuid.uuid4().hex + "." + extension
    path = os.path.join(folder, secure_filename(name))

    file.save(path)
    return name


def save_video(file, folder, allowed):
    extension = get_extension(file.filename)

    if extension not in allowed:
        raise ValueError("Unsupported video format.")

    name = uuid.uuid4().hex + "." + extension
    path = os.path.join(folder, secure_filename(name))

    file.save(path)
    return name

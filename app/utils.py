import os
import secrets
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename

def save_profile_picture(form_picture):
    # Generate a random name for the file to avoid name conflicts
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    
    # Ensure the file is safe to store
    picture_filename = random_hex + file_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)
    
    # Save the picture to the specified directory
    form_picture.save(picture_path)
    
    return picture_filename



def delete_picture(picture_filename):
    if picture_filename != 'default.jpg':
        picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], picture_filename)
        if os.path.exists(picture_path):
            os.remove(picture_path)

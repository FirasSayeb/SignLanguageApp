from flask import Flask, render_template, request, send_file, url_for
from moviepy.editor import ImageSequenceClip
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESIZED_FOLDER = 'resized_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(RESIZED_FOLDER):
    os.makedirs(RESIZED_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('textarea')
    image_paths = []

   
    char_to_image = {
        'a': 's1.png',
        'b': 's2.png',
        'c': 's3.png',
        'd': 's4.png',
        'e': 's5.png',
        'f': 's6.png',
        'g': 's7.png',
        'h': 's8.png',
        'i': 's9.png',
        'j': 's10.png',
        'k': 's11.png',
        'l': 's12.png',
        'm': 's13.png',
        'n': 's14.png',
        'o': 's15.png',
        'p': 's16.png',
        'q': 's17.png',
        'r': 's18.png',
        's': 's19.png',
        't': 's20.png',
        'u': 's21.png',
        'v': 's22.png',
        'w': 's23.png',
        'x': 's24.png',
        'y': 's25.png',
        'z': 's26.png'
    }

    target_size = (640, 480)  

    for letter in text.lower(): 
        if letter in char_to_image:
            image_path = os.path.join(app.root_path, 'static', char_to_image[letter])
            resized_path = os.path.join(RESIZED_FOLDER, char_to_image[letter])
            with Image.open(image_path) as img:
                img = img.resize(target_size, Image.Resampling.LANCZOS)
                img.save(resized_path)
                image_paths.append(resized_path)

    if image_paths:
        clip = ImageSequenceClip(image_paths, fps=1) 
        video_path = os.path.join(UPLOAD_FOLDER, 'output_video.mp4')
        clip.write_videofile(video_path, fps=24) 

        return send_file(video_path, as_attachment=True)
    else:
        return "No valid characters to convert to images."

if __name__ == "__main__":
    app.run(debug=True)

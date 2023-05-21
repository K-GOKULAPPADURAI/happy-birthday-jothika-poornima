from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Folder path for content
content_folder = 'content'

# Route for home page
@app.route('/')
def home():
    # Get list of image and video files in the content folder
    images = [file for file in os.listdir(os.path.join(content_folder, 'images')) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    videos = [file for file in os.listdir(os.path.join(content_folder, 'videos')) if file.endswith(('.mp4', '.avi', '.mov', '.wmv'))]
    
    return render_template('index.html', images=images, videos=videos)

# Route to serve images
@app.route('/content/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(content_folder, 'images'), filename)

# Route to serve videos
@app.route('/content/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory(os.path.join(content_folder, 'videos'), filename)

if __name__ == '__main__':
    app.run()

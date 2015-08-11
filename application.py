from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
import frame_grabber as fg
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['mp4', 'png', 'jpg', 'mov'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index(filename=None):
    return render_template('index.html', filename=filename)

@app.route('/present', methods=['GET', 'POST'])
def show():
    results = fg.get_logos_matrix('./video_csvs', 'cats.csv')
    return render_template('index2.html', results=results)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/import', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file_upload']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fg.do_videos(UPLOAD_FOLDER, './video_csvs', save_time=0.5) 
            return index(filename)
    return


if __name__ == "__main__":
    port = os.getenv('VCAP_APP_PORT', '5000')
    app.run(host='0.0.0.0', port=int(port),debug=True)

from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['mp4', 'png', 'jpg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

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
            #return redirect(url_for('uploaded_file',
            #                        filename=filename))
            return render_template('index.html')
    return

if __name__ == "__main__":
    app.run(debug=True)
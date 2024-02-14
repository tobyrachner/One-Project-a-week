import os, sys
from flask import Blueprint, render_template, request, send_from_directory, redirect, url_for, current_app
from werkzeug.utils import secure_filename




views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/create', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        file = request.files['img']
        
        filename = secure_filename(file.filename)
        file.save(current_app.config['UPLOAD_FOLDER'] + filename)
        return redirect(url_for('views.view_images', name=filename))

    return render_template('create.html')

@views.route('/images/<name>')
def view_images(name):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], name)
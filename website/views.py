import os, sys
from flask import Blueprint, render_template, request, send_from_directory, redirect, url_for, current_app
from werkzeug.utils import secure_filename
from .models import Project
from . import db




views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/create', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        name = request.form.get('name').replace(' ', '_')
        description = request.form.get('description')
        date = request.form.get('date')
        file = request.files['img']
        
        filename = secure_filename(file.filename)
        file_type = filename.split('.')[-1]
        file.save(current_app.config['UPLOAD_FOLDER'] + name + '.' + file_type)

        
        new_project = Project(name=name, description=description, date=date)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('views.view_images', name=name))

    return render_template('create.html')

@views.route('/project/<name>')
def view_images(name):
    project = Project.query.filter_by(name=name).first()
    if not project:
        return '<p>Project not Found</p>'

    return name
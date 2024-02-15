import os, sys
from flask import Blueprint, render_template, request, send_from_directory, redirect, url_for, current_app
from werkzeug.utils import secure_filename
from .models import Project
from . import db




views = Blueprint('views', __name__)

@views.route('/')
def home():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)

@views.route('/create', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        name = request.form.get('name')
        lower_name = name.lower().replace(' ', '_')
        description = request.form.get('description')
        date = request.form.get('date')
        file = request.files['img']
        
        filename = secure_filename(file.filename)
        file_type = filename.split('.')[-1]
        path = '../static/images/' + lower_name + '.' + file_type
        file.save(current_app.config['UPLOAD_FOLDER'] + lower_name + '.' + file_type)

        
        new_project = Project(name=name, lower_name=lower_name, description=description, path=path, date=date)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('views.view_project', name=lower_name))

    return render_template('create.html')

@views.route('/project/<name>')
def view_project(name):
    project = Project.query.filter_by(lower_name=name).first()
    if not project:
        return '<p>Project not Found</p>'

    return name
import os, sys
from flask import Blueprint, render_template, request, send_from_directory, redirect, url_for, current_app
from werkzeug.utils import secure_filename
from .models import Project, Tag
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
        tags = request.form.get('tags')
        file = request.files['img']
        
        filename = secure_filename(file.filename)
        file_type = filename.split('.')[-1]
        path = '../static/images/' + lower_name + '.' + file_type
        file.save(current_app.config['UPLOAD_FOLDER'] + lower_name + '.' + file_type)
        
        for tag in tags.split(', '):
            if tag == '':
                continue
            check = Tag.query.filter_by(name=tag).first()
            if not check:
                db.session.add(Tag(name=tag))

        new_project = Project(name=name, lower_name=lower_name, description=description, tags=tags, path=path, date=date)
        db.session.add(new_project)
        db.session.commit()
        print(Tag.query.all())
        return redirect(url_for('views.view_project', name=lower_name))

    return render_template('create.html')

@views.route('/project/<name>')
def view_project(name):
    project = Project.query.filter_by(lower_name=name).first()
    if not project:
        return '<p>Project not Found</p>'

    return render_template('project.html', project=project)
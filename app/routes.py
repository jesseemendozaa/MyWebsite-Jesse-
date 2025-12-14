from flask import render_template
from datetime import datetime

def init_app(app):

    @app.route("/")
    def home():
        year = datetime.now().year
        return render_template("home.html", year=year)

    @app.route("/about")
    def about():
        year = datetime.now().year
        return render_template("about.html", year=year)
    
    @app.route("/resume")
    def resume():
        year = datetime.now().year
        return render_template("resume.html", year=year)
    
    @app.route("/heritage")
    def heritage():
        year = datetime.now().year
        return render_template("heritage.html", year=year)

    @app.route("/projects")
    def projects():
        year = datetime.now().year
        return render_template("projects.html", year=year)
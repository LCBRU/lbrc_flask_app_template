from .. import blueprint
from flask import render_template


@blueprint.route("/")
def index():
    return render_template("ui/index.html")


@blueprint.route("/another")
def another():
    return render_template("ui/another.html")


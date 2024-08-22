from .. import blueprint
from flask import render_template, request
from lbrc_flask.forms import SearchForm
from lbrc_flask.database import db
from sqlalchemy import select
from lbrc_flask.security import User


@blueprint.route("/")
def index():
    search_form = SearchForm(formdata=request.args)

    q = select(User)

    if search_form.search.data:
        q = q.filter(User.username.like(f'%{search_form.search.data}%'))

    users = db.paginate(
        select=q,
        page=search_form.page.data,
        per_page=5,
        error_out=False,
    )

    return render_template(
        "ui/index.html",
        users=users,
        search_form=search_form,
    )


@blueprint.route("/another")
def another():
    return render_template("ui/another.html")


@blueprint.route("/dialog")
def dialog():
    return render_template("ui/dialog.html")

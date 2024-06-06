from flask import Blueprint, render_template

bp = Blueprint('directions', __name__)


@bp.route('/directions')
def index():
    return render_template('directions/index.html')

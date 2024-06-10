import os

import markdown
from flask import Blueprint, render_template

bp = Blueprint('directions', __name__)
template_dir = os.path.join(os.path.dirname(__file__), 'templates')


@bp.route('/directions')
def index():
    title = "Directions"
    address = "1234 Park Place, Birmingham, AL"
    with open(os.path.join(template_dir, "directions\\directions_text.md"), "r", encoding="utf-8") as f:
        text = f.read()
    text_directions_src = markdown.markdown(text)
    map = './static/images/sample-map.png'

    template_vars = {
        'title': title,
        'address': address,
        'directions': text_directions_src,
        'map': map
    }

    return render_template('/directions/index.html', **template_vars)

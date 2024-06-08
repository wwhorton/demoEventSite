from flask import Blueprint, render_template

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    cards = [
        {
            'image': '',
            'title': '',
            'text': ''
        },
        {
            'image': '',
            'title': '',
            'text': ''
        },
        {
            'image': '',
            'title': '',
            'text': ''
        }
    ]
    template_vars = {
        'title': "Backyard Barbecue 2024",
        'subtitle': "We're back with the best barbecue of the summer!",
        'button_text': "Get Directions",
        'subheading': "Taste ten years of tradition",
        'cards': cards,
        'blurb': '',
        'blurb_img': ''
    }

    return render_template('home/index.html', **template_vars)

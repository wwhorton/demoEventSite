import markdown
from flask import Blueprint, render_template

bp = Blueprint('about', __name__)


@bp.route('/about')
def index():
    with open("demoEventSite/templates/about/about_text_1.md", "r", encoding="utf-8") as f:
        text = f.read()
    body_content_1 = markdown.markdown(text)
    with open("demoEventSite/templates/about/about_text_2.md", "r", encoding="utf-8") as f:
        text = f.read()
    body_content_2 = markdown.markdown(text)
    template_variables = {
        "heading": "About the Backyard Picnic",
        "subheading": "Ten years and still going strong!",
        "hero_image": "https://placehold.co/1280x650",
        "inset_image_1": 'https://placehold.co/600x400',
        "inset_image_2": 'https://placehold.co/600x400',
        "body_content_1": body_content_1,
        "body_content_2": body_content_2,
    }

    return render_template('/about/index.html', title="About", **template_variables)

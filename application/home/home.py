"""General page routes."""
from flask import Blueprint, render_template

# Blueprint Configuration
home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/home/static')


@home_bp.route('/', methods=['GET'])
def home():
    """ Homepage """
    return render_template("index.html")


@home_bp.route('/about', methods=['GET'])
def about():
    """ About """
    return render_template("about.html")

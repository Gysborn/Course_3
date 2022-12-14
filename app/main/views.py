from flask import Blueprint, render_template, abort

from app.dao.main_dao import get_posts_all, get_id_bookmarks

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def index_page():
    """
    Выводит стартовую страничку
    :return: 'index.html'
    """
    try:
        all_posts = get_posts_all()
    except:
        return abort(404)
    return render_template('index.html', all_posts=all_posts, bookmarks=get_id_bookmarks())


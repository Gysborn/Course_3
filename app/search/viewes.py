from flask import Blueprint, request, render_template, abort

from app.dao.main_dao import search_for_posts, get_id_bookmarks

search_blueprint = Blueprint('search_blueprint', __name__)


@search_blueprint.route('/search')
def search_page():
    """
    Находит посты по ключевому слову
    :return: Шаблон html с найденными постами и закладками
    """
    try:
        query = request.args.get("s").lower()
        posts = search_for_posts(query)
    except:
        return abort(404)
    return render_template('search.html', posts=posts, bookmarks=get_id_bookmarks())

from flask import Blueprint, render_template
from werkzeug.utils import redirect

from app.dao.main_dao import get_post_by_pk, save_to_bookmarks, get_bookmarks

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__)


@bookmarks_blueprint.route('/bookmarks/add/<post_id>')
def add_bookmarks(post_id):
    """
    функция добавления закладок
    :param post_id: число id поста
    :return:
    """
    post = get_post_by_pk(post_id) # вытягиваем пост по ай ди
    bookmarks = get_bookmarks() # вытягиваем все закладки
    bookmarks.append(post) # лепим новый пост к закладкам
    save_to_bookmarks(bookmarks) # сохраняем обновленный файл bookmarks.json
    return redirect('/', code=302) # переадресуем на главную


@bookmarks_blueprint.route('/bookmarks')
def show_all_bookmarks():
    return render_template('index.html', all_posts=get_bookmarks())

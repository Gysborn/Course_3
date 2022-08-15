from flask import Blueprint, render_template, abort
from werkzeug.utils import redirect

from app.dao.main_dao import save_to_bookmarks, get_id_bookmarks, get_bookmarks_by_id

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__)


@bookmarks_blueprint.route('/bookmarks/add/<post_id>')
def add_bookmarks(post_id):
    """
    функция добавления закладок
    :param post_id: число id поста
    :return:
    """
    bookmarks = get_id_bookmarks() # вытягиваем все закладки
    bookmarks.append(int(post_id))  # лепим новый пост к закладкам
    save_to_bookmarks(bookmarks)  # сохраняем обновленный файл bookmarks.json
    return redirect('/', code=302)  # переадресуем на главную


@bookmarks_blueprint.route('/bookmarks/remove/<post_id>')
def remove_bookmarks(post_id):
    """
    Удаляет закладки из bookmarks.json
    :param post_id: по идентификатору поста
    :return:
    """
    bookmarks = get_id_bookmarks() # получаем все закладки
    bookmarks.remove(int(post_id))  # удаляем
    save_to_bookmarks(bookmarks)  # сохраняем новый список

    return redirect('/', code=302)  # переадресуем на главную


@bookmarks_blueprint.route('/bookmarks')
def show_all_bookmarks():
    """
    выводим все закладки
    :return:
    """
    return render_template('bookmarks.html', posts=get_bookmarks_by_id())

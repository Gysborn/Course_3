from flask import Blueprint, render_template

from app.dao.main_dao import get_post_by_pk, get_comments_by_post_id, tag_replace, get_id_bookmarks

post_blueprint = Blueprint('post_blueprint', __name__)


@post_blueprint.route('/post/<post_id>', methods=["GET", "POST"])
def post_page(post_id):
    """
    открывает конкретный пост по идентификатору
    :param post_id: идентификатор поста
    :return:
    """
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    post['content'] = tag_replace(post['content']) # оборачивает в теги слова с решеткой
    return render_template('post.html', post=post, comments=comments, bookmarks=get_id_bookmarks())

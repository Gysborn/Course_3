from flask import Blueprint, render_template

from app.dao.main_dao import get_post_by_pk, get_comments_by_post_id

post_blueprint = Blueprint('post_blueprint', __name__)


@post_blueprint.route('/post/<post_id>', methods=["GET", "POST"])
def post_page(post_id):
    current_post = get_post_by_pk(post_id)
    if not current_post:
        return "<span class='item__username'>Такого поста не существует</span>"
    else:
        get_comments_by_post_id(post_id)
        return render_template('post.html', current_post=current_post, comments=get_comments_by_post_id(post_id))

from flask import Blueprint, render_template, abort

from app.dao.main_dao import get_posts_by_user

user_feed_blueprint = Blueprint('user_feed_blueprint', __name__)


@user_feed_blueprint.route('/user-feed/<name>')
def user_feed(name):
    user_posts = get_posts_by_user(name)
    if not user_posts:
        return abort(404)
    return render_template('user-feed.html', user_posts=user_posts, name=name)

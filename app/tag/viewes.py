from flask import Blueprint, render_template

from app.dao.main_dao import get_posts_all

tag_blueprint = Blueprint('tag_blueprint', __name__)


@tag_blueprint.route('/tag/food')
def tag_food_page():
    tag_posts = []
    posts = get_posts_all()
    for post in posts:
        if 'food' in post['tags']:
            tag_posts.append(post)
    return render_template('tag_food.html', posts=tag_posts)


@tag_blueprint.route('/tag/cat')
def tag_cat_page():
    tag_posts = []
    posts = get_posts_all()
    for post in posts:
        if 'cat' in post['tags']:
            tag_posts.append(post)
    return render_template('tag_cat.html', posts=tag_posts)


@tag_blueprint.route('/tag/insta')
def tag_insta_page():
    tag_posts = []
    posts = get_posts_all()
    for post in posts:
        if 'insta' in post['tags']:
            tag_posts.append(post)

    return render_template('tag_insta.html', posts=tag_posts)


@tag_blueprint.route('/tag/travel')
def tag_travel_page():
    tag_posts = []
    posts = get_posts_all()
    for post in posts:
        if 'travel' in post['tags']:
            tag_posts.append(post)
    return render_template('tag_travel.html', posts=tag_posts)
import json
from flask import request
POST_PATH = 'data/data.json'
COMMENTS_PATH = 'data/comments.json'
BOOKMARKS_PATH = 'data/bookmarks.json'


def get_posts_all():
    with open(POST_PATH, encoding='utf-8') as file:
        all_posts = json.load(file)
    return all_posts


def get_post_by_pk(pk) -> dict:
    """all_posts = get_posts_all()
    for post in all_posts:
        if post['pk'] == int(pk):
            return post
    return False
    """
    all_posts = get_posts_all()
    return all_posts[int(pk) - 1]


def search_for_posts(qwery):
    posts = get_posts_all()
    posts_found = []
    if not posts:
        return "<p><a href='/' class='link'>Файл не открывается. Назад</a></p>"

    for post in posts:
        if qwery in post["content"].lower():
            posts_found.append(post)

    return posts_found


def get_comments_by_post_id(post_id):
    with open(COMMENTS_PATH, encoding='utf-8') as file:
        all_comments = json.load(file)
        post_comments = []
        for comments in all_comments:
            if comments["post_id"] == int(post_id):
                post_comments.append(comments)
    return post_comments


def save_to_bookmarks(new_json: list):
    """
    Сохраняет в файл обновленный лист со словарями закладок.
    :param new_json:
    :return:
    """
    with open(BOOKMARKS_PATH, 'w', encoding='utf-8') as file:
        json.dump(new_json, file, ensure_ascii=False)


def get_bookmarks():
    """

    :return: Список закладок
    """
    with open(BOOKMARKS_PATH, encoding='utf-8') as file:
        all_bookm = json.load(file)
    return all_bookm



def get_posts_by_user(user_name):
        pass


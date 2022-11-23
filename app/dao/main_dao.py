import json
from typing import List

from flask import abort

from app.exeptions import BadRequest

POST_PATH = 'data/data.json'
COMMENTS_PATH = 'data/comments.json'
BOOKMARKS_PATH = 'data/bookmarks.json'


def tag_replace(content_post):
    """

    :param content_post:
    :return: #слова в посте обернув в тег
    """
    food = ['#еда', '#пирог', '#завтраком', '#едой', '#завтраком']
    insta = ['#инста', '#красивый', '#лампочка', '#инстаграм', '#инстарамная', '#фото', '#елки', '#птицы', '#показали']
    cat = ['#котом']
    travel = ['#попутчика', '#катере', '#обследовать']


    tag_food = "<a href='/tag/food'>#</a>"
    tag_cat = "<a href='/tag/cat'>#</a>"
    tag_insta = "<a href='/tag/insta'>#</a>"
    tag_travel = "<a href='/tag/travel'>#</a>"
    while True:
        i = content_post.find(' #')# получаем индекс начала тега
        if i == -1:
            break
        w = [] # тут будет #слово
        i += 1 # что бы убрать пробел
        c = ' .,-?!' #определяем до каких символов отрезать слово
        while content_post[i] not in c: # запускаем цикл: пока не равен символу из строки с
            w += content_post[i] # составляем слово-тег
            i += 1
        word = ''.join(w) # преобразуем в строку
        if word in food:
            tag = tag_food.replace("#", word)
        elif word in cat:
            tag = tag_cat.replace("#", word)
        elif word in insta:
            tag = tag_insta.replace("#", word)
        else:
            tag = tag_travel.replace("#", word)

        content_post = content_post.replace(word, tag)
    return content_post


def get_posts_all():
    """

    :return: все посты из файла
    """
    with open(POST_PATH, encoding='utf-8') as file:
        all_posts = json.load(file)
    return all_posts


def get_post_by_pk(pk) -> List[str]:
    """

    :param pk:
    :return: возвращает пост по ай ди
    """

    all_posts = get_posts_all()
    try:
        post = all_posts[int(pk) - 1]
    except IndexError:
        raise BadRequest(name='Index out range', description='Индекс вне диапазона')
    except ValueError:
        raise BadRequest(name='Value error', description='Значение не является числом')
    return post


def search_for_posts(query):
    """

    :param query:
    :return: посты по совпадению с ключем
    """
    posts_found = []
    try:
        posts = get_posts_all()
    except BadRequest:
        raise BadRequest(name='Some error', description='Что то пошло не так')

    for post in posts:
        if query.lower() in post["content"].lower():
            posts_found.append(post)

    return posts_found


def get_comments_by_post_id(post_id):
    """

    :param post_id:
    :return: все комменты к данному посту
    """
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


def get_id_bookmarks():
    """

    :return: Список закладок
    """
    with open(BOOKMARKS_PATH, encoding='utf-8') as file:
        all_bookm = json.load(file)
    return all_bookm


def get_bookmarks_by_id():
    """

    :return: список id постов преобразует в посты
    """
    bookmarks = get_id_bookmarks() # получаем айдишники всех постов в закладках
    all_posts = get_posts_all() # получаем все посты
    bookmark_post = [] # создаем пустой лист для закладок
    for bookmark in bookmarks:
        bookmark_post.append(all_posts[bookmark - 1]) # по ай ди выцепляем посты и складыаем в лист
    if not bookmark_post:
        raise BadRequest(name='Some error', description='Ничего не найдено')
    return bookmark_post


def get_posts_by_user(user_name):
    """

    :param user_name:
    :return: конкретный пост
    """
    posts = get_posts_all()
    user_posts = []

    for post in posts:
        if post["poster_name"] == user_name:
            user_posts.append(post)
    return user_posts

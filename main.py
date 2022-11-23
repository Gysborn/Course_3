
from flask import Flask, jsonify, abort, Response, json
import logging


from app.bookmarks.viewes import bookmarks_blueprint
from app.dao.main_dao import get_posts_all, get_post_by_pk
from app.exeptions import BadRequest
from app.search.viewes import search_blueprint

from app.main.views import main_blueprint

from app.post.views import post_blueprint
from app.tag.viewes import tag_blueprint
from app.user_feed.viewes import user_feed_blueprint

logger_one = logging.getLogger("one") #создаем экзкмпляр логгера
logger_one.setLevel("DEBUG")
file_handler = logging.FileHandler("Logs/api.log")
#создаем хендлер для записи в файл
file_handler.setLevel("DEBUG")
formatter_one = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
# создаем форматтер для вывода текущего времени, уровня и сообщения
file_handler.setFormatter(formatter_one)
# инициализируем форматтер в хендлере
logger_one.addHandler(file_handler)
# добавляем инициализированный хендлер в логгер


# Настраиваем его на максимальную чувствительность
# Ура! Логгер настроен!
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Регистрируем первый блюпринт
app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(tag_blueprint)


@app.route('/api/posts')
def get_posts():
    logger_one.info("/api/posts")
    try:
        posts = get_posts_all()
    except:
        return abort(404)
    return jsonify(posts)


@app.route('/api/posts/<post_id>')
def get_post_id(post_id):
    logger_one.info(f"/api/posts/{post_id}")
    return get_post_by_pk(post_id)


@app.errorhandler(404)
def not_found(error):
    logger_one.debug("Ошибочный запрос")
    return "Ничего не нашлось!", 404



@app.errorhandler(BadRequest)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = Response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": 400,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    response.status = 400
    return response
    #return "Ошибка 418 Индекс вне диапазона!", 418


if __name__ == '__main__':
    app.run(debug=True)

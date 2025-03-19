# app.py

# импорт модуля Flask, который вы ранее установили с помощью
# pip install Flask==2.2.2 "connexion[swagger-ui]==2.14.1"
from flask import render_template
import connexion

# создание экземпляра приложения с использованием Connexion, а не Flask
# Внутри приложение Flask все еще создается, но теперь к нему добавлены
# дополнительные функции.
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/") # декоратор функции для "/" (корневого URL веб-приложения)
def home():
    return render_template("home.html") # функция, выводящая home.html в качестве шаблона

if __name__ == "__main__":
    # основной вызов приложения с указанием хоста и порта
    app.run(host="0.0.0.0", port=8000)

from flask import Flask, render_template
app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/" },
    {  "title": "Мобы", "URL": "/mobs" },
    { "title": "Контакты", "URL": "/contacts" },
    { "title": "Обо мне", "URL": "/about" },
    { "title": "Глоссарий", "URL": "/glossary" }
]
mob = [
    {"title": "Скелет", "URL": "/skeleton"},
    {"title": "Зомби", "URL": "/spider"},
    {"title": "Паук", "URL": "/zombie"},
    {"title": "Эндермен", "URL": "/enderman"},
    {"title": "Крипер", "URL": "/creeper"}
]

@app.context_processor
def global_context():
    return{
        "nav": nav
    }
@app.route("/glossary")
def glossary_view():
    return render_template("/glossary.html",name = "Глоссарий")

@app.route("/skeleton")
def skeleton_view():
    return render_template("mobss/skeleton.html", name = "Скелет")

@app.route("/zombie")
def zombie_view():
    return render_template("mobss/zombie.html", name = "Зомби")

@app.route("/spider")
def spider_view():
    return render_template("mobss/spider.html", name = "Паук")

@app.route("/enderman")
def ender_view():
    return render_template("mobss/enderman.html", name = "Эндермен")

@app.route("/creeper")
def creeper_view():
    return render_template("mobss/creeper.html", name = "Крипер")

@app.route("/")
def hello_world():
    return render_template("main.html", name="Главная")

@app.route("/about")
def about_view():
    return render_template("about.html", name="Обо мне")

@app.route("/contacts")
def contacts_view():
    return render_template("contacts.html", name="Контакты")

@app.route("/mobs")
def mob_view():
    return render_template("mobs.html", name="Мобы")
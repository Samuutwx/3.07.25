# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
def leer_ideas():
    try:
        with open('ideas.txt', 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def guardar_idea(idea):
    with open('ideas.txt', 'a', encoding='utf-8') as f:
        f.write(idea + '\n')


@app.route('/ideas', methods=['GET', 'POST'])
def ideas():
    if request.method == 'POST':
        idea = request.form['idea']
        if idea.strip():
            guardar_idea(idea)
    lista_ideas = leer_ideas()
    return render_template('ideas.html', ideas=lista_ideas)


if __name__ == "__main__":
    app.run(debug=True)

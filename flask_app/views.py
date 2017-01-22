from flask import render_template, request, redirect, url_for, session
from flask_app import app
from models import add_gif, get_gifs, star_gif, get_starred, add_user, get_user, clear_db

@app.route('/')
def index():
    #clear_db()
    user_id = session.get('Gifiphy')
    if not user_id or not get_user(user_id):
        new_id = add_user()
        session['Gifiphy'] = new_id

    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
	search = request.form['search']
        gifs, max_slides = backend.fetch_gifs(search)
        user = get_user(session.get('Gifiphy'))
        user.current_max = int(max_slides)
        [add_gif(g, s, user) for (g,s) in gifs]

        return redirect(url_for('chose'))

@app.route('/chose')
def chose():
    user = get_user(session.get('Gifiphy'))
    gifs = get_gifs(user)
    return render_template('chose.html', gifs=gifs) 

@app.route('/add_to_presentation/<id>')
def add_to_presentation(id):
    star_gif(id)
    user = get_user(session.get('Gifiphy'))
    if user.current_slide == user.current_max:
        link = backend.get_link(get_starred(user))
        return redirect(url_for('download', link=link))
    return redirect(url_for('chose'))

@app.route('/download/<link>')
def download(link):
    clear_db(session.get('Gifiphy'))
    return render_template('download.html', link=link)

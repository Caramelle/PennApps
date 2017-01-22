from flask import render_template, request, redirect, url_for, session
from flask_app import app, db
from models import add_gif, get_gifs, add_user, get_user, clear_db, get_gif
from flask_app.backend import findGif, findText

@app.errorhandler(500)
def server_error(e):
    return redirect(url_for('index'))

@app.route('/')
def index():
    user_id = session.get('Gifiphy')
    if not user_id or not get_user(user_id):
        new_id = add_user()
        session['Gifiphy'] = new_id

    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
	search = request.form['search']
        
        gifs = findGif.fetch_gifs(search)
        max_slides = len(gifs)

        user = get_user(session.get('Gifiphy'))
        user.current_max = max_slides
        user.presentation_url = search

        for i in xrange(max_slides):
            [add_gif(g, i, user) for g in gifs[i]]

        return redirect(url_for('chose'))

@app.route('/chose')
def chose():
    user = get_user(session.get('Gifiphy'))
    if user.current_slide == user.current_max:
        return redirect(url_for('download'))

    gifs = get_gifs(user)
    if not gifs:
        return redirect(url_for('chose'))

    return render_template('chose.html', gifs=gifs) 

@app.route('/add_to_presentation/<id>')
def add_to_presentation(id):
    user = get_user(session.get('Gifiphy'))
    if int(id)>=0:
        g = get_gif(id)
        findText.add_image(user.presentation_url, g.url, g.number)
    if user.current_slide == user.current_max:
        return redirect(url_for('download'))
    return redirect(url_for('chose'))

@app.route('/download')
def download():
    link = get_user(session.get('Gifiphy')).presentation_url
    clear_db(session.get('Gifiphy'))
    return render_template('download.html', link=link)

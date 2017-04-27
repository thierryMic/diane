from werkzeug.contrib.cache import SimpleCache
from flask import Flask, render_template, request, redirect, jsonify, url_for, json
from flask import session, flash, make_response

from flask_seasurf import SeaSurf
# from flask.ext.seasurf import SeaSurf

import os
import sys

from db.database import Member, Gallery, Painting, get, getOne, getTable, getSort
import login

cache = SimpleCache()
app = Flask(__name__)
csrf = SeaSurf(app)
app.config['UPLOAD_FOLDER'] = '/var/www/itemcatalog/static/img'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



def render(template, **kw):

    """Helper function for rendering templates.

    This function includes a list of categories, a flag to indicate whether a
    Member is logged, any other keyword arguments passed in by the calling
    calling function and calls the Flask's render_template function.

    Args:
      template  : the template we want to render
      **kw      : a list of keyword arguments to pass to the template.

    Returns     : Returns a HTTP response with the relevant template.
    """
    galleries=cache.get('galleries')
    if not galleries:
    # if cache.has("galleries"):
        cache.set('galleries', getTable(Gallery))
        galleries=cache.get('galleries')

    loggedIn = 'provider' in session
    return render_template(template, galleries=galleries, loggedIn=loggedIn, **kw)


@app.route('/')
@app.route('/index/')
def index():

    """Returns a page with the 10 most recent items."""
    return render('index.html')



@app.route('/works')
def works():

    """Returns a page with the 10 most recent items."""
    return render('works.html', title="Galleries")


@app.route('/gallery/<int:galleryId>')
def gallery(galleryId):

    """Returns a page for a specified category.

    Retrieves items belonging to the specified category and renders them as
    the category's page.

    Args:
      categoryId : the id of the category to display.

    Returns      : Returns a HTTP response with the category template.
    """

    paintings = get(Painting, "galleryId", galleryId)
    gallery = getOne(Gallery, "galleryId", galleryId).name
    return render('gallery.html', title=gallery, paintings=paintings)


@app.route('/paintings/JSON')
def paintingsJSON():

    """Returns a JSON object representing all the paintings in the database."""

    paintings = getTable(Painting)
    return jsonify(paintings=[p.serialize for p in paintings])


@app.route('/prices/')
def prices():
    paintings = getTable(Painting)
    return render('prices.html', title="Prices", paintings=paintings)



@app.route('/about/')
def about():
    return render('about.html', title="About Diane")




@app.route('/painting/<int:paintingId>')
def painting(paintingId):

    painting = getOne(Painting, "paintingId", paintingId)
    return render('painting.html', p=painting)


def startServer():

    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    startServer()


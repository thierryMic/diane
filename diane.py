
from flask import Flask, render_template, request, redirect, jsonify, url_for, json
from flask import session, flash, make_response

from flask_seasurf import SeaSurf
# from flask.ext.seasurf import SeaSurf

import itertools
import memcache
import os
import sys

from db.database import Member, Gallery, Painting, get, getOne, getTable, getSort
import login

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
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
    # galleries=cache.get('galleries')
    # if 'galleries' not in locals():
    # if cache.has("galleries"):
        # cache.set('galleries', getTable(Gallery))
    galleries=getTable(Gallery)

    loggedIn = 'provider' in session
    return render_template(template, galleries=galleries, loggedIn=loggedIn, **kw)


def getGallery(galleryId):
    key = 'g%s' % galleryId
    gallery = mc.get(key)
    if not gallery:
        print 'adding gallery %s to cache' % galleryId
        gal = getOne(Gallery, "galleryId", galleryId).name
        paintings = get(Painting, "galleryId", galleryId)
        gallery = {'galName':gal, 'paintings':paintings}
        mc.set(key, gallery)
        print gallery
    return gallery



@app.route('/')
@app.route('/index/')
def index():

    """Returns a page with the 10 most recent items."""
    return render('index.html')



@app.route('/works')
def works():
    return render('works.html', title="Galleries")


@app.route('/gallery/<int:galleryId>')
def gallery(galleryId):
    gallery = getGallery(galleryId)
    return render('gallery.html', title=gallery['galName'], paintings=gallery['paintings'])



@app.route('/prices/')
def prices():
    paintings = getTable(Painting)
    return render('prices.html', title="Prices", paintings=paintings)



@app.route('/about/')
def about():
    return render('about.html', title="About Diane")


def getPainting(paintingId):
    key ='p%s' % paintingId
    painting = mc.get(key)
    if not painting:
        painting = getOne(Painting, "paintingId", paintingId)
        gallery = getGallery(painting.galleryId)
        paintings = gallery['paintings']

        for i in range(len(paintings)):
            if paintings[i].paintingId == paintingId:
                pre = len(paintings) - 1 if i == 0 else i - 1
                nex = 0 if i == len(paintings) - 1 else i + 1

        painting = {'pre':paintings[pre].paintingId, 'painting':painting,
                    'nex':paintings[nex].paintingId}
        mc.set(key, painting)
    return painting


@app.route('/painting/<int:paintingId>')
def painting(paintingId):
    p = getPainting(paintingId)
    return render('painting.html', p=p['painting'], pre=p['pre'], nex=p['nex'])




@app.route('/test/<int:galleryId>')
def test(galleryId):
    key = 'gal%s' % galleryId
    gallery = mc.get(key)
    if not gallery:
        print 'adding to cache'
        gal = getOne(Gallery, "galleryId", galleryId).name
        paintings = get(Painting, "galleryId", galleryId)
        gallery = {'galName':gallery, 'paintings':paintings}
        mc.set(key, gallery)

    return render('gallery.html', title=gallery['galName'], paintings=gallery['paintings'])


def startServer():

    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)



if __name__ == '__main__':
    startServer()


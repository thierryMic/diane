
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
    loggedIn = 'provider' in session
    return render_template(template, galleries=getGalleries(), loggedIn=loggedIn, **kw)


def getGalleries():
    key = 'galleries'
    galleries = mc.get(key)
    if not galleries:
        galleries=getTable(Gallery)
        mc.set(key, galleries)
    return galleries


def getGallery(galleryId):
    key = 'g%s' % galleryId
    gallery = mc.get(key)
    if not gallery:
        gal = getOne(Gallery, "galleryId", galleryId).name
        paintings = get(Painting, "galleryId", galleryId)
        json = jsonify(paintings=[p.serialize for p in paintings])
        gallery = {'galName':gal, 'paintings':paintings, 'json':json}
        mc.set(key, gallery)
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


@app.route('/mainPaints/JSON/<string:size>')
def mainPaintsJSON(size):
    galleries=getGalleries()
    return jsonify(paintings=['%s%s.jpg' %
                              (url_for('static', filename='img/%s' % g.image), size)
                              for g in galleries])


@app.route('/gallery/JSON/<int:galleryId>')
def galleryJSON(galleryId):
    gallery = getGallery(galleryId)
    return gallery['json']



def startServer():

    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)



if __name__ == '__main__':
    startServer()


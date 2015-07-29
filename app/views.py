"""
===============================================================================

    This file is part of muServe.

    muServe is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    muServe is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with muServe; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

=============================================================================*/
###############################################################################

    Copyright (C) 2015 Kushagra Singh

###############################################################################
"""

from flask import Flask, render_template, request, redirect, url_for, session
from models import Queue
from app import muServe, db



@muServe.route('/')
def home():
    return redirect(url_for('queue'))

# extracts current song from file
# if not found, plays Knife Party's - Bonfire

@muServe.route("/current")
def current():
    f = open("app/current.txt", "r")
    currsong = f.read()
    currsong = currsong.split("\n")

    if len(currsong) == 3:
        return str(currsong[0]) + "\n" + str(currsong[1]) + "\n" + str(currsong[2])
    else:
        f.close()
        f = open("app/current.txt", "w")

        try:
            allsong = Queue.query.all()
            allsong.sort(key = lambda x : x.upvote, reverse = True)
            song = allsong[0]
            stringtowrite = str(song.songid) + "\n" + str(song.name) + "\n" + str(song.upvote)
            db.session.delete(song)
            db.session.commit()
        except:
            stringtowrite = "e-IWRmpefzE\nKnife Party - 'Bonfire'\n1"

        f.write(stringtowrite)
        f.close()
        return stringtowrite

@muServe.route("/currentcount")
def currentcount():
    allsong = Queue.query.all()
    return str(len(allsong))

@muServe.route('/queue')
def queue():
    links = []
    queued = Queue.query.all()
    count = 0

    for i in queued:
        links.append(i)
        count += 1

    currsong = {}
    currinfo = current().split("\n")
    currsong["currname"] = currinfo[1]

    return render_template('queue.html', allvids = links, currentsong = currsong,
                            songcount = count)

# next song
@muServe.route("/next")
def next():
    allsong = Queue.query.all()
    allsong.sort(key = lambda x : x.upvote, reverse = True)

    try:
        song = allsong[0]
        newsong = str(song.songid) + "\n" + str(song.name) + "\n" + str(song.upvote)
        db.session.delete(song)
        db.session.commit()
    except:
        newsong = "e-IWRmpefzE\nKnife Party - 'Bonfire'\n1"

    f = open("app/current.txt", "w")
    f.write(newsong)
    f.close()

    return newsong


@muServe.route("/play")
def play():
    currsong = current()
    currsong = currsong.split("\n")

    currentsong = {}
    currentsong["id"] = currsong[0]
    currentsong["name"] = currsong[1]
    currentsong["votes"] = currsong[2]

    return render_template('play.html', song = currentsong)


# Add /queue. This is public. Now playing plus up next and upvotes.

@muServe.route('/search')
def search():
    return render_template('search.html')

@muServe.route('/add/<path:link>', methods = ['GET', 'POST'])
def add(link):
    if request.method == 'POST':
        found = Queue.query.get(link)

        if found == None:
            newsong = Queue(songid = link, name = request.form["title"], upvote = 1)
            db.session.add(newsong)
            db.session.commit()
            print "added"
            session[link] = "1"
            return redirect(url_for('play'))
        else:
            try:
                print session[link]
                print "already upped"
            except:
                print "upvoting"
                found.upvote += 1
                session[link] = "1"
                db.session.add(found)
                db.session.commit()

            return redirect(url_for('play'))
    else:
        return redirect(url_for('search'))

if __name__ == "__main__":
    muServe.run(debug = True)


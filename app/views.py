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

@muServe.route("/")
@muServe.route('/welcome')
def welcome():
    return render_template('welcome.html')

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
            return redirect(url_for('welcome'))

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

            return redirect(url_for('welcome'))


    else:
        return redirect(url_for('search'))

if __name__ == "__main__":
    muServe.run(debug = True)


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

from flask import Flask, render_template

muserve = Flask(__name__)

@muserve.route("/")
def hello():
    return "Hello World!"

@muserve.route('/welcome')
def welcome():
    return render_template('welcome.html')

@muserve.route('/search')
def search():
    return render_template('search.html')

if __name__ == "__main__":
    muserve.run(debug = True)
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

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

muServe = Flask(__name__)
muServe.config.from_object('config')
db = SQLAlchemy(muServe)

from app import views, models
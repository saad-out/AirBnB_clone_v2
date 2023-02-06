#!/usr/bin/python3
"""
Flask application for complete dynamic AirBnB wepage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(error):
    """
    Close session
    """
    storage.close()


@app.route('/hbnb')
def hbnb():
    """
    Dynamic AirBnb webpage
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

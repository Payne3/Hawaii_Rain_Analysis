import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)




@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/Measurement<br/>"
        f"/api/v1.0/Station"
    )

@app.route("/api/v1.0/Measurement")
def Measurement():
    """Return a list of all measurements we want"""
    # Query Rain measurements for last year
    results = session.query(Measurement.date, Measurement.prcp,).filter(Measurement.date > "2016-08-22").order_by(Measurement.date).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query the measurables
    results = session.query(Measurement.date, Measurement.prcp,).filter(Measurement.date > "2016-08-22").order_by(Measurement.date).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    Measurements = []
    for date, prcp in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        Measurements.append(measurement_dict)

    return jsonify(all_passengers)



if __name__ == '__main__':
    app.run(debug=True)
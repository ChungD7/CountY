#!/usr/bin/env python3
"""
    Jeff Ondich, 22 April 2016
    Modified by CS257 Team E, March 2020
"""
import flask
from flask import render_template, request
import sys
import psycopg2
import math
sys.path.append('backend')
from datasource import *

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = DataSource()


@app.route('/')
def homePage():
    return render_template('homePage.html', states=db.getListOfStates())

@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route("/results", methods=["GET", "POST"])
def results():
    """Handles form submission. Navigating to this route manually yields nationwide voting results."""
    if request.method == "POST":
        results = db.getCountiesInShareRange(request.form.get("partyC"), request.form.get("startC"), request.form.get("endC"), request.form.get("state"))
        displayable = results[0] != "bad request"
        return render_template('resultsPageAreaList.html', result = results, display = displayable)

    # if user reached route via navbar 'Results' tab
    else:
        votes = db.getTotalVotesUSA()
        dem_share = db.getPartyPercentageUSA("dem")
        rep_share = db.getPartyPercentageUSA("rep")
        third_share = db.getPartyPercentageUSA("third")
        other_share = db.getPartyPercentageUSA("other")

        return render_template('resultsPagePercentComparison.html', total_votes=votes,
                               dem_percent=round(dem_share * 100, 2),
                               rep_percent=round(rep_share * 100, 2),
                               third_percent=round(third_share * 100, 2),
                               other_percent=round(other_share * 100, 2),
                               dem_votes=int(dem_share * float(votes)),
                               rep_votes=int(rep_share * float(votes)),
                               third_votes=int(third_share * float(votes)),
                               other_votes=int(other_share * float(votes))
                               )

@app.route("/outcome", methods=["GET", "POST"])
def outcome():
    if request.method == "POST":
        results = db.getStatesInShareRange(request.form.get("partyS"), request.form.get("startS"), request.form.get("endS"))
        displayable = results[0] != "bad request"
        return render_template('resultsPageAreaList.html', result = results, display = displayable)


"""routes to resultpage based on state click interaction from homepage"""
@app.route('/search/<state>/')
def search(state):
    votes = db.getTotalVotesInState(state)
    dem_share = db.getPartyPercentageS("dem", state)
    rep_share = db.getPartyPercentageS("rep", state)
    third_share = db.getPartyPercentageS("third", state)
    other_share = db.getPartyPercentageS("other", state)

    county_list = db.getCountiesInState(state)

    return render_template('resultsPagePercentComparison.html', total_votes=votes,
                           dem_percent=round(dem_share * 100, 2),
                           rep_percent=round(rep_share * 100, 2),
                           third_percent=round(third_share * 100, 2),
                           other_percent=round(other_share * 100, 2),
                           dem_votes=int(dem_share * float(votes)),
                           rep_votes=int(rep_share * float(votes)),
                           third_votes=int(third_share * float(votes)),
                           other_votes=int(other_share * float(votes)),
                           counties=county_list
                           )


"""routes to resultpage based on selected county"""
@app.route('/search/<rawstate>/<rawcounty>/')
def search_county(rawstate, rawcounty):
    state = ''.join(str(elem) for elem in rawstate.split("%20"))
    county = ''.join(str(elem) for elem in rawcounty.split("%20"))
    votes = db.getTotalVotesInCounty(county, state)
    dem_share = db.getPartyPercentageC("dem", county, state)
    rep_share = db.getPartyPercentageC("rep", county, state)
    third_share = db.getPartyPercentageC("third", county, state)
    other_share = db.getPartyPercentageC("other", county, state)

    county_list = db.getCountiesInState(state)

    return render_template('resultsPagePercentComparison.html', total_votes=votes,
                           dem_percent=dem_share,
                           rep_percent=rep_share,
                           third_percent=third_share,
                           other_percent=other_share,
                           dem_votes=int(float(dem_share) * float(votes) / 100),
                           rep_votes=int(float(rep_share) * float(votes) / 100),
                           third_votes=int(float(third_share) * float(votes) / 100),
                           other_votes=int(float(other_share) * float(votes) / 100),
                           counties=county_list
                           )


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    app.run(host=sys.argv[1], port=sys.argv[2])

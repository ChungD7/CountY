import MySQLdb
import getpass
import math

class DataSource:
    """
    DataSource executes all of the queries on the database.
    It also formats the data to send back to the frontend, typically in a list
    or some other collection or object.
    """

    def __init__(self):
        self.connection = MySQLdb.connect(host="edwardlee.mysql.pythonanywhere-services.com",
                     user="edwardlee",
                     passwd="mahjames",
                     db="edwardlee$electiondata")
        self.cur = self.connection.cursor()

    def getListOfStates(self):
        """
            Returns a list of al the states in the database
            PARAMETERS:
                none
            RETURN:
                a list of all states
        """
        self.cur.execute("SELECT DISTINCT state from electiondata ORDER BY state;")
        states_response = [i[0] for i in self.cur.fetchall()]
        return states_response


    def getTotalVotesInCounty(self, county, state):
        """
            Returns the number of total votes casted in specified county.
            PARAMETERS:
                county
                state
            RETURN:
                an int of the number of total votes casted in this county
        """

        self.cur.execute(
            "SELECT SUM(totalvotes) FROM electiondata WHERE area = '" + county + "' AND state = '" + state + "'")

        return self.cur.fetchone()[0]


    def getTotalVotesInState(self, state):
        """
            Returns the number of total votes casted in specified state.
            PARAMETERS:
                state
            RETURN:
                an int of the number of total votes casted in this state
        """

        self.cur.execute("SELECT SUM(totalvotes) FROM electiondata WHERE state = '" + state + "'")

        return self.cur.fetchone()[0]

    def getTotalVotesUSA(self):
        """
            Returns the number of total votes casted nationwide.
            PARAMETERS:
                none
            RETURN:
                an int of the number of total votes casted nationwide
        """

        self.cur.execute("SELECT SUM(totalvotes) FROM electiondata")

        return self.cur.fetchone()[0]

    def getCountiesInState(self, state):
        """
            Returns a list of the counties that make up the specified state.
            PARAMETERS:
                state
            RETURN:
                a list of all of the counties that make up this state
        """

        self.cur.execute("SELECT area from electiondata WHERE state = '" + state + "'")
        counties_response = [i[0] for i in self.cur.fetchall()]
        return counties_response

    def getPartyPercentageC(self, party, county, state):
        """
            Returns the percentage of total votes garnered by specified party within specified county.
            PARAMETERS:
                party
                    in the form of 'rep' 'dem' 'third' or 'other' for compatibility with our SQL database
                county
                state
            RETURN:
                a decimal or percentage of total votes garnered by this party within this county.
        """

        self.cur.execute(
            "SELECT " + party + "votespercent FROM electiondata WHERE area = '" + county + "' AND state = '" + state + "'")

        return self.cur.fetchone()[0]


    def getPartyPercentageS(self, party, state):
        """
            Returns the percentage of total votes garnered by specified party within specified state.
            PARAMETERS:
                party
                state
            RETURN:
                a decimal or percentage of total votes garnered by this party within this state.
        """

        self.cur.execute("SELECT SUM(" + party + "votes) FROM electiondata WHERE state = '" + state + "'")
        sum = self.cur.fetchone()[0]
        self.cur.execute("SELECT SUM(totalvotes) FROM electiondata WHERE state = '" + state + "'")

        partyPercent = sum / self.cur.fetchone()[0]
        return partyPercent

    def getPartyPercentageUSA(self, party):
        """
            Returns the percentage of total votes garnered by specified party, nationwide.
            PARAMETERS:
                party
            RETURN:
                a decimal or percentage of total votes garnered by this party, nationwide.
        """

        self.cur.execute("SELECT SUM(" + party + "votes) FROM electiondata;")
        sum = self.cur.fetchone()[0]
        self.cur.execute("SELECT SUM(totalvotes) FROM electiondata;")

        partyPercent = sum / self.cur.fetchone()[0]
        return partyPercent

    def getCountiesInShareRange(self, party, start, end, state=None):
        """
            Returns a list of all of the counties in the specified state in which the specified party percentage resides within the specified starting
             and ending percentages (inclusive). If state is not entered, the function searches from all the counties in the country.
            PARAMETERS:
                start - the low bound of the party percentage range
                end - the high bound of the party percentage range
                party
                state
            RETURN:
                a list of all of the counties in the state with the specified party percentage in the specified range.
        """

        if state and state != "":
            self.cur.execute("SELECT area, state FROM electiondata WHERE state = '" + state + "' AND " + party + "votespercent BETWEEN " + start + " and " + end)
        else:
            self.cur.execute("SELECT area, state FROM electiondata WHERE " + party + "votespercent BETWEEN " + start + " and " + end)
        output = self.cur.fetchall()


        if len(output) > 75:
            return ["bad request", "Found " + str(len(output)) + " results. Please narrow your range."]
        elif len(output) == 0:
            return ["bad request", "No counties found in specified range."]
        else:
            return output


    def getStatesInShareRange(self, party, start, end):
        """
            Returns a list of all of the states in which the largest party percentage resides within the specified starting
             and ending percentages (inclusive).
            PARAMETERS:
                start - the low bound of the party percentage range
                end - the high bound of the party percentage range
            RETURN:
                a list of all of the states with the largest party percentage in the specified range.
        """

        output = []

        the_states = self.getListOfStates()
        for state in the_states:
            if float(start)/100 <= self.getPartyPercentageS(party, state) <= float(end)/100:
                output.append(state)

        if len(output) == 0:
            return ["bad request", "No states found in specified range."]
        else:
            return output

    def __del__(self):
        self.cur.close()
        self.connection.close()

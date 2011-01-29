#!/usr/bin/python
"""
A Parser for the "sessiontable" section of the EZProxy /status page
"""

from datetime import datetime, date, time
from HTMLParser import HTMLParser

def parse_isodate( data ):
    """Parse a 'YYYY-MM-DD HH:MM:SS' string and return a dattime object"""

    ( d_str, t_str ) = data.split(" ")

    ( year, month, day ) = d_str.split( "-" )
    ( hour, minute, second ) = t_str.split( ":" )

    return datetime.combine(
        date( int( year ), int( month ), int( day ) ),
        time( int( hour ), int( minute ), int( second ) )
    )

class EZPSessionParser( HTMLParser ):
    """
    A Parser for the "sessiontable" section of the EZProxy /status page
    """
    # pylint: disable=R0904

    found_session_table = False
    found_session_tr = False
    found_session_td = 0
    found_session_a = False
    sessions = {}
    session = None

    def handle_starttag( self, tag, attrs ):

        if tag == "table" and self.found_session_table is not True:
            if ( "id", "sessiontable" ) in attrs:
                self.found_session_table = True

        if tag == "tr" and self.found_session_table is True:
            self.found_session_tr = True
            for attr in attrs:
                if attr[0] == "id":
                    self.sessions[ attr[1] ] = {}
                    self.session = attr[1]

        if tag == "td" and self.found_session_tr is True:
            self.found_session_td += 1

        # Session
        if tag == "a" and self.found_session_td == 1:
            self.found_session_a = True
            for attr in attrs:
                if attr[0] == "href":
                    self.sessions[ self.session ][ "href" ] = attr[1]

    def handle_endtag( self, tag ):

        if tag == "table" and self.found_session_table is True:
            self.found_session_table = False

        if tag == "tr" and self.found_session_tr is True:
            self.found_session_tr = False
            self.found_session_td = 0
            self.session = None

        if tag == "td" and self.found_session_td is True:
            pass

        if tag == "a" and self.found_session_a is True:
            self.found_session_a = False

    def handle_data(self, data):

        if self.found_session_a is True:
            self.sessions[ self.session ][ "session" ] = data
        # Username
        if self.found_session_td == 2:
            if data != "Username":
                self.sessions[ self.session ][ "username" ] = data
        # From
        if self.found_session_td == 3:
            if data != "From":
                self.sessions[ self.session ][ "from" ] = data
        # Created
        if self.found_session_td == 4:
            if data != "Created":
                self.sessions[ self.session ][ "created" ] = parse_isodate( data )
        # Accessed
        if self.found_session_td == 5:
            if data != "Accessed":
                self.sessions[ self.session ][ "accessed" ] = parse_isodate( data )
        # Generic
        if self.found_session_td == 6:
            if data != "Generic":
                self.sessions[ self.session ][ "generic" ] = data

if __name__ == '__main__':
    import gzip

    PARSER = EZPSessionParser()
    PARSER.feed( gzip.open( "test/status.html.gz", "rb" ).read() )

    for session in PARSER.sessions:
        print PARSER.sessions[ session ]

# vim:expandtab:ts=4

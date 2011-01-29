#!/usr/bin/python
"""
A Parser for the release data from the EZProxy /status page
"""

import datetime
import re
from HTMLParser import HTMLParser

class EZPReleaseParser( HTMLParser ):
    """
    A Parser for the release data from the EZProxy /status page
    """
    # pylint: disable=R0904

    found_first_h1 = False

    data = {
        'release': {},
        'validation': {},
    }

    release_regex = r"EZproxy (?P<major>\S+)\.(?P<minor>\S+) (?P<line>\S+) for "
    release_regex += "(?P<os>\S+) started at "
    release_regex += "(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) "
    release_regex += "(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})"
    release = re.compile( release_regex )

    validation_regex = r"EZproxy was last able to validate the license on "
    validation_regex += "(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) "
    validation_regex += "(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})"
    validation = re.compile( validation_regex )

    def handle_starttag( self, tag, attrs ):

        if tag == "h1" and self.found_first_h1 is not True:
                self.found_first_h1 = True

        if tag == "h2" and self.found_first_h1 is True:
                self.found_first_h1 = False

    def handle_data(self, data):

        if self.found_first_h1 is True:

            match = self.release.search( data )
            if match is not None:
                started = datetime.datetime( 
                    int( match.group( 'year' ) ), int( match.group( 'month' ) ), 
                    int( match.group( 'day') ), int( match.group( 'hour' ) ), 
                    int( match.group( 'minute' ) ), int( match.group( 'second') )
                )
                self.data['release'] = {
                    'version': "%s.%s" % ( match.group( 'major' ), match.group( 'minor' ) ),
                    'line': match.group( 'line' ),
                    'os': match.group( 'os' ),
                    'started': started,
                }

            match = self.validation.search( data )
            if match is not None:
                validated = datetime.datetime( 
                    int( match.group( 'year' ) ), int( match.group( 'month' ) ), 
                    int( match.group( 'day') ), int( match.group( 'hour' ) ), 
                    int( match.group( 'minute' ) ), int( match.group( 'second') )
                )
                self.data['validation'] = validated

if __name__ == '__main__':
    import gzip

    PARSER = EZPReleaseParser()
    PARSER.feed( gzip.open( "test/status.html.gz", "rb" ).read() )

    print PARSER.data

# vim:expandtab:ts=4

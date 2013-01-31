#!/usr/bin/python
"""
A Parser for the "miscellaneous" section of the EZProxy /status page
"""

import re
from HTMLParser import HTMLParser

class EZPMaintParser( HTMLParser ):
    """
    A Parser for the "maintenance" section of the EZProxy /status page
    """
    # pylint: disable=R0904

    found_maint_a = False
    found_maint_form = False

    data = {
        # Remove %d orphaned host%s that %s !!! database index%s (requires EZproxy restart)<br>
        'm1': {
            'regex': re.compile( 'Remove (?P<count>\d+) orphaned hosts? that \S+ !!! database indexe?s?' ),
            'restart': True,
            'count': 0,
        },
        # Remove %d host%s that %s not been used in over 30 days (requires EZproxy restart)
        'm2': {
            'regex': re.compile( 'Remove (?P<count>\d+) hosts? that \S+ not been used in over 30 days' ),
            'restart': True,
            'count': 0,
        },
        # Shutdown %d port%s that %s previously assigned for proxy by port (no restart required)
        'm3': {
            'regex': re.compile( 'Shutdown (?P<count>\d+) ports? that \S+ previously assigned for proxy by port' ),
            'restart': False,
            'count': 0,
        },
        # Reset accessed and referenced dates and counts of all hosts (no restart required)
        'm4': {
            'label': 'reset dates and counts',
            'regex': re.compile( 'Reset accessed and referenced dates and counts of all hosts' ),
            'restart': False,
        },
        # Compress port usage by reassigning higher ports into any available gaps (no restart required)
        'm5': {
            'label': 'compress port usage',
            'regex': re.compile( 'Compress port usage by reassigning higher ports into any available gaps' ),
            'restart': False,
        },
    }

    def handle_starttag( self, tag, attrs ):

        if tag == "a" and self.found_maint_a is not True:
            if ( "name", "hostmaintenance" ) in attrs:
                self.found_maint_a = True

        if tag == "form" and self.found_maint_a:
            self.found_maint_form = True

        # Error out if a new Host Maintenance is added that we don't know about
        if tag == "input" and self.found_maint_form:
            if ( "type", "radio" ) in attrs:
                for ( key, value ) in attrs:
                    if key == "value" and value != '':
                        try:
                            assert( value in self.data.keys() )
                        except AssertionError:
                            raise ValueError( "The %r radio option does not represent a known hostmaintenance action" % ( value ) )

    def handle_endtag( self, tag ):
        if tag == "form" and self.found_maint_form:
            self.found_maint_form = False

    def handle_data(self, data):

        if self.found_maint_form is True:
            for key in self.data.keys():
                if self.data[key].has_key('regex'):
                    match = self.data[key]['regex'].search( data )
                    if match != None:
                        try:
                            self.data[key]['count'] = match.group('count')
                        except IndexError:
                            pass
                        del self.data[key]['regex']

if __name__ == '__main__':
    import gzip

    PARSER = EZPMaintParser()
    PARSER.feed( gzip.open( "test/status.html.gz", "rb" ).read() )

    print PARSER.data
# vim:expandtab:ts=4

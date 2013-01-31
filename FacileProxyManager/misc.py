#!/usr/bin/python
"""
A Parser for the "miscellaneous" section of the EZProxy /status page
"""

from HTMLParser import HTMLParser

class EZPMiscParser( HTMLParser ):
    """
    A Parser for the "miscellaneous" section of the EZProxy /status page
    """
    # pylint: disable=R0904

    found_misc_a = False

    data = {
        'sessions_active': 0,
        'sessions_limit': 0,
        'transfers_active': 0,
        'transfers_limit': 0,
        'hosts_peak': 0,
        'hosts_limit': 0,
        'ssl_init': False,
    }

    def handle_starttag( self, tag, attrs ):

        if tag == "a" and self.found_misc_a is not True:
            if ( "name", "miscellaneous" ) in attrs:
                self.found_misc_a = True

    def handle_data(self, data):

        if self.found_misc_a is True:

            if data.startswith( "Peak sessions active/limit:" ):
                values = data.split( ":" )[1].strip( " \n" )
                ( active, limit ) = values.split( "/" )
                self.data[ 'sessions_active' ] = int( active )
                self.data[ 'sessions_limit' ] = int( limit )

            if data.startswith( "Peak concurrent transfers active/limit:" ):
                values = data.split( ":" )[1].strip( " \n" )
                ( active, limit ) = values.split( "/" )
                self.data[ 'transfers_active' ] = int( active )
                self.data[ 'transfers_limit' ] = int( limit )

            if data.startswith( "Peak virtual hosts/limit:" ):
                values = data.split( ":" )[1].strip(" \n")
                ( peak, limit ) = values.split( "/" )
                self.data[ 'hosts_peak' ] = int( peak )
                self.data[ 'hosts_limit' ] = int( limit )

            if data.startswith( "SSL is initialized" ):
                self.data[ 'ssl_init' ] = True

if __name__ == '__main__':
    import gzip

    PARSER = EZPMiscParser()
    PARSER.feed( gzip.open( "test/status.html.gz", "rb" ).read() )

    print PARSER.data

# vim:expandtab:ts=4

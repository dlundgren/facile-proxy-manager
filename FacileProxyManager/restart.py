#!/usr/bin/python
"""
A Parser for the EZProxy /restart page
"""

from HTMLParser import HTMLParser

class EZPRestartParser( HTMLParser ):
    """
    A Parser for the EZProxy /restart page
    """
    # pylint: disable=R0904

    pid = None

    def handle_starttag( self, tag, attrs ):
        if tag == "input":
            if ( "name", "pid" ) in attrs:
                for ( key, value ) in attrs:
                    if key == "value":
                        self.pid = value

if __name__ == '__main__':
    import gzip

    PARSER = EZPRestartParser()
    PARSER.feed( gzip.open( "test/restart.html.gz", "rb" ).read() )

    print PARSER.pid

# vim:expandtab:ts=4

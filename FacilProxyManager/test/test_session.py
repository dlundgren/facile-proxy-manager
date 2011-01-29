"""
Unit tests for EZPSessionParser
"""

import gzip
import unittest

from FacilProxyManager import session

def suite():
    """Return a pre-built test suite"""

    tests = [
        'test_sessions'
    ]

    return unittest.TestSuite(
        [ TestEZPSessionParser( test ) for test in tests ]
    )

class TestEZPSessionParser( unittest.TestCase ):
    """
    Unit tests for EZPSessionParser
    """

    def setUp( self ):
        # pylint: disable=C0103
        self.parser = session.EZPSessionParser()
        self.parser.feed( gzip.open( "status.html.gz", "rb" ).read() )

    def test_sessions( self ):
        """Test session parsing"""

        self.assertEqual( len( self.parser.sessions ), 4968 )

if __name__ == '__main__':
    unittest.TextTestRunner( verbosity=2 ).run( suite() )

# vim:expandtab:ts=4

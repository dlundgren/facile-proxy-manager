"""
Unit tests for EZPReleaseParser
"""

import datetime
import gzip
import unittest

from FacileProxyManager import release

def suite():
    """Return a pre-built test suite"""

    tests = [ 
        'test_release_started',
        'test_release_version',
        'test_release_line',
        'test_release_os',
        'test_validation_time',
    ]

    return unittest.TestSuite(
        [ TestEZPReleaseParser( test ) for test in tests ] 
    )

class TestEZPReleaseParser( unittest.TestCase ):
    """
    Unit tests for EZPReleaseParser
    """
    # pylint: disable=R0904

    def setUp( self ):
        # pylint: disable=C0103
        self.parser = release.EZPReleaseParser()
        self.parser.feed( gzip.open( "status.html.gz", "rb" ).read() )

    def test_release_started( self ):
        """Check server start time"""

        self.assertEqual(
            self.parser.data[ "release" ][ "started" ], 
            datetime.datetime(2011, 1, 24, 8, 32, 51) 
        )

    def test_release_version( self ):
        """Check server version"""

        self.assertEqual( self.parser.data[ "release" ][ "version" ], "5.2" )

    def test_release_line( self ):
        """Check server code line"""

        self.assertEqual( self.parser.data[ "release" ][ "line" ], "GA" )

    def test_release_os( self ):
        """Check server OS"""

        self.assertEqual( self.parser.data[ "release" ][ "os" ], "Linux" )

    def test_validation_time( self ):
        """Check license validation"""

        self.assertEqual(
            self.parser.data[ "validation" ],
            datetime.datetime(2011, 1, 24, 8, 32, 52)
        )

if __name__ == '__main__':
    unittest.TextTestRunner( verbosity=2 ).run( suite() )

# vim:expandtab:ts=4

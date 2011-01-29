"""
Unit tests for EZPMiscParser
"""

import gzip
import unittest

from FacilProxyManager import misc

def suite():
    """Return a pre-built test suite"""

    tests = [ 
        'test_sessions_active', 
        'test_sessions_limit', 
        'test_transfers_active', 
        'test_transfers_limit', 
        'test_hosts_peak', 
        'test_hosts_limit', 
        'test_ssl_init'
    ]

    return unittest.TestSuite(
        [ TestEZPMiscParser( test ) for test in tests ] 
    )

class TestEZPMiscParser( unittest.TestCase ):
    """
    Unit tests for EZPMiscParser
    """
    # pylint: disable=R0904

    def setUp( self ):
        # pylint: disable=C0103
        self.parser = misc.EZPMiscParser()
        self.parser.feed( gzip.open( "status.html.gz", "rb" ).read() )

    def test_sessions_active( self ):
        """Check sessions active"""

        self.assertEqual( self.parser.data[ "sessions_active" ], 5001 )

    def test_sessions_limit( self ):
        """Check sessions limit"""

        self.assertEqual( self.parser.data[ "sessions_limit" ], 6000 )

    def test_transfers_active( self ):
        """Check transfers active"""

        self.assertEqual( self.parser.data[ "transfers_active" ], 872 )

    def test_transfers_limit( self ):
        """Check transfers limit"""

        self.assertEqual( self.parser.data[ "transfers_limit" ], 1000 )

    def test_hosts_peak( self ):
        """Check peak hosts"""

        self.assertEqual( self.parser.data[ "hosts_peak" ], 62 )

    def test_hosts_limit( self ):
        """Check hosts limit"""

        self.assertEqual( self.parser.data[ "hosts_limit" ], 200 )

    def test_ssl_init( self ):
        """Check SSL status"""

        self.assertEqual( self.parser.data[ "ssl_init" ], True )

if __name__ == '__main__':
    unittest.TextTestRunner( verbosity=2 ).run( suite() )

# vim:expandtab:ts=4

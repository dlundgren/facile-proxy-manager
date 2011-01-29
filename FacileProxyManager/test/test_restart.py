"""
Unit tests for EZPRestartParser
"""

import gzip
import unittest

from FacileProxyManager import restart

def suite():
    """Return a pre-built test suite"""

    tests = [ 
        'test_pid'
    ]

    return unittest.TestSuite(
        [ TestEZPRestartParser( test ) for test in tests ] 
    )

class TestEZPRestartParser( unittest.TestCase ):
    """
    Unit tests for EZPRestartParser
    """

    def setUp( self ):
        # pylint: disable=C0103
        self.parser = restart.EZPRestartParser()
        self.parser.feed( gzip.open( "restart.html.gz", "rb" ).read() )

    def test_pid( self ):
        """Test PID parsing"""

        self.assertEqual( self.parser.pid, "1234" )

if __name__ == '__main__':
    unittest.TextTestRunner( verbosity=2 ).run( suite() )

# vim:expandtab:ts=4

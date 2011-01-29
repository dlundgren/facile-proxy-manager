"""Facil Proxy Manager files"""

class ServerNotEZProxy( Exception ):
    """Raised when the 'Server' header in the reply is not 'EZproxy'"""

    def __init__( self, value ):
        super( Exception, self ).__init__( value )
        self.server = value

    def __str__( self ):
        return "Not connected to EZProxy (%s)" % ( self.server )

# vim:expandtab:ts=4

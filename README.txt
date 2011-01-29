===================
Facil Proxy Manager
===================

Facil Proxy Manager provides a scriptable interface for OCLC's EZProxy.  This 
can be particularly useful when a large number of operations need performed
against the server --  such as clearing out a large number of sessions --
without having to do each operation by hand in a web browser.

Initial setup
=============

Facil Proxy Manager creates a settings directory under ~/.FacilProxyManager 
where it stores the following files::

* ~/.FacilProxyManager/config

This is a ConfigParser-formatted configuration file.  It allows you to set
global default values, as well as server-specific settings.  This file will be
created and populated with sample values the first time the program is run.
Server-specific settings can be added to their own section, which will
override the default values.

* ~/.FacilProxyManager/history

This file is populated with the history of commands executed within the
program.

Configuration Settings
----------------------

The following variables are available to be set::

*host*
	This variable defines the EZProxy server name.

	Defaults to 'localhost.localdomain'

*port*
	This variable defines the EZProxy port number.

	Defaults to 2048

*cookiename*
	This variable defines the EZProxy cookie name.

	Defaults to 'ezproxy'

*ssl*
	This variable defines if a SSL certificate has been installed on the
	server.

	Defaults to 'False'

*username*
	This variable sets the username used to login to EZProxy.  The user
	entry in users.txt will need to be flagged as an administrative
	account.  For example::

		admin:password:admin

	Defaults to 'admin'

*password*
	This variable sets the password used to login to EZProxy.

	Defaults to 'password'

*testing*
	If this variable is set to 'True', read-only operations will be the
	only allowed operations.  Server restarts, sesstion termination, and
	other operations that are not passive in nature will not be performed.

	Defaults to 'True'

Multiple Servers
----------------------

The section handling functionality of ConfigParser is used to configure 
FacilProxyManager for multiple servers.  To setup 2 servers, one using SSL
certificates, and the other using port 80, the following lines would be added
to the config file::

[server1.example.com]
ssl=True

[server2.example.com]
port=80

The rest of the settings for these servers will come from the [DEFAULT]
section of the config file.

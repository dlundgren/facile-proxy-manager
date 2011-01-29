"""
Distutils packaging for Facil Proxy Manager
"""

from distutils.core import setup

setup(
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    license='GPL',
    name='FacilProxyManager',
    version='0.1.0',
    maintainer="Andrew Anderson",
    maintainer_email='andrew@lirn.net',
    url='http://www.lirn.net/',
    packages=[
        'FacilProxyManager',
    ],
    scripts=[
        'bin/facil-proxy-manager', 
    ],
    package_dir={ },
    package_data={ },
    data_files=[ ],
    description = "A command line interface to OCLC's EZProxy",
    long_description = """
A command line interface for interacting with OCLC's EZProxy product, 
enabling scripted interaction with the server instead of using a web browser.
    """
)

# vim:expandtab:ts=4

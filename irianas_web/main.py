#!/usr/bin/env python
""":mod:`irianas_web.main` -- Program entry point
"""
<<<<<<< HEAD
from flask import Flask
from modules.login import irianas_module as login
from modules.home import irianas_module as home
from modules.clients import irianas_module as clients
from modules.http import irianas_module as http
from modules.ftp import irianas_module as ftp
from modules.dns import irianas_module as dns
from modules.mysql import irianas_module as mysql
from modules.servers import irianas_module as servers
from modules.client import irianas_module as client
from modules.list_user_ftp import irianas_module as list_user_ftp
from modules.user_ftp import irianas_module as user_ftp
from modules.cambio_password_ftp import irianas_module as cambio_password_ftp
from modules.crear_virtual import irianas_module as crear_virtual
from modules.list_domain import irianas_module as list_domain

app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(clients)
app.register_blueprint(http)
app.register_blueprint(ftp)
app.register_blueprint(dns)
app.register_blueprint(mysql)
app.register_blueprint(servers)
app.register_blueprint(client)
app.register_blueprint(list_user_ftp)
app.register_blueprint(user_ftp)
app.register_blueprint(cambio_password_ftp)
app.register_blueprint(crear_virtual)
app.register_blueprint(list_domain)

if __name__ == '__main__':
    app.run(debug=True)
=======

from __future__ import print_function

import argparse
import sys

from irianas_web import metadata


def main(argv):
    """Program entry point.

    :param argv: command-line arguments
    :type argv: :class:`list`
    """
    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    epilog = '''
{project} {version}

{authors}
URL: <{url}>
'''.format(
        project=metadata.project,
        version=metadata.version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)
    arg_parser.add_argument(
        '-v', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))

    arg_parser.parse_args(args=argv[1:])

    print(epilog)

    return 0


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()
>>>>>>> 02abb1edfadf0bc22d392a10d174e85cdc08dfa0

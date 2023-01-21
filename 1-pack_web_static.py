#!/usr/bin/python3
"""
This module packs web_static to deploy
"""


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """
    from fabric.api import local

    local("mkdir -p versions")
    ret = local('tar -cvzf "versions/web_static_$(date \'+%Y%m%d%H%M%S\').tgz"\
                web_static')
    if ret.succeeded:
        return 'versions/'
    else:
        return None

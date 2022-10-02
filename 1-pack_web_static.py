#!/usr/bin/python3
"""
fabric script that generates .tgz archive from web_static contents
"""
from fabric.api import *
import time


def do_pack():
    """function to generate tgz archive"""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/"
              .format(timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except FileNotFoundError:
        return None

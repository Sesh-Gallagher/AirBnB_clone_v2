#!/usr/bin/python3
"""
Represents Fabric script that generates a .tgz 
archive from the contents of the web_static """

from fabric.api import *
from datetime import datetime

def do_pack():
    """
    Module that makes  an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
<<<<<<< HEAD
=======
~                     
>>>>>>> 9f9ea85fb58d31533aa44595e8592e903526659f

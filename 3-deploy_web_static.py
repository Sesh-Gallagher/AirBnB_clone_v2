#!/usr/bin/python3
"""Represents Fabric script based on the file 2-do_deploy_web_static.py
that creates anddistributes an archive to the web servers

execute: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu"""

import os.path
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['54.208.52.184', '34.227.90.100']


def do_pack():
    """ Module that generate an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except Exception:
        return None


def do_deploy(archive_path):
    """Module to distribute an archive to web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except Exception:
        return False


def deploy():
    """Module to create and distributes an archive to web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except Exception:
        return False

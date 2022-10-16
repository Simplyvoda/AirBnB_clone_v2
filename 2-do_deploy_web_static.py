#!/usr/bin/python3
"""
distributes archives to web servers using do_deploy
"""
from fabric.api import put, run, env
from os.path import exists
env.hosts=['3.236.23.23', '3.238.196.183']
env.user='ubuntu'
env.key_filename='~/.ssh/school'
env.password=None


def do_deploy(archive_path):
    """Do deploy function"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        n = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, n))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, n))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, n))
        run('sudo rm -rf {}{}/web_static'.format(path, n))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, n))
        run('sudo chmod -R 755 /data/')
        print("New version deployed!")
        return True
    except FileNotFoundError:
        return False

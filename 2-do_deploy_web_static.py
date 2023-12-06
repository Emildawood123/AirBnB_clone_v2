#!/usr/bin/python3
"depoly by fabric"
from fabric.api import *
from fabric import task
from datetime import datetime
import os


@task
def do_pack():
    """archive web_static"""
    try:
        time_now = datetime.now().strftime('%Y%m%d%H%M%S')
        nameOfFile = 'web_static_{}.tgz web_static'.format(time_now)
        local("mkdir -p versions")
        local("tar -cvzf versions/{}".format(nameOfFile))
        return "versions/"
    except Exception:
        return None


@task
def do_deploy(archive_path):
    """deploy web_static to servers"""
    env.hosts = ['35.153.79.242', '52.201.164.137']
    if not os.path.exists(archive_path):
        return False
    try:
        for host in env.hosts:
            env.host_string = host
            web_static = "/data/web_static"
            filename = archive_path.split('/')[-1]
            update_filename = filename.split('.')[0]
            put(archive_path, '/tmp/')
            run(f'mkdir -p {web_static}/releases/{update_filename}/')
            run(f'tar -xzf /tmp/{update_filename}.tgz -C \
                {web_static}/releases/{update_filename}/')
            run(f'rm /tmp/{update_filename}.tgz')
            run(f'mv {web_static}/releases/{update_filename}/web_static/* \
                {web_static}/releases/{update_filename}/')
            run(
                f'rm -rf {web_static}/releases/{update_filename}/web_static')
            run(f'rm -rf {web_static}/current')
            run(f'ln -s {web_static}/releases/{update_filename}/ \
                {web_static}/current')
            print('New version deployed!')

        return True
    except Exception:
        return False

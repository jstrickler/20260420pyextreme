import os
from configparser import ConfigParser
import paramiko
from paramiko import Transport, SFTPClient

config = ConfigParser()
config.read('sdfauth.ini')

LOCAL_FILE = '../DATA/mary.txt'
REMOTE_DIR = 'text_files'

# create paramiko Transport instance
with Transport((config['auth']['hostname'], 22)) as transport:
    transport.connect(
        username=config['auth']['username'], 
        password=config['auth']['password']
    )  # connect to remote host

    # create SFTP client using Transport instance
    with SFTPClient.from_transport(transport) as sftp: 
        # get list of items on default (login) folder (listdir_iter() returns an iterator)
        remote_files = sftp.listdir()
        print(f"{remote_files = }")

        # create remote dir
        if REMOTE_DIR not in remote_files:
            sftp.mkdir(REMOTE_DIR)
        
        REMOTE_PATH = os.path.join(REMOTE_DIR, os.path.basename(LOCAL_FILE))
        sftp.put(LOCAL_FILE, REMOTE_PATH)
        print(f"{sftp.listdir() = }")
        print(f"{sftp.listdir(REMOTE_DIR) = }")
        
        sftp.unlink(REMOTE_PATH)
        print(f"{sftp.listdir(REMOTE_DIR) = }")

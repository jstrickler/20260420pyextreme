from configparser import ConfigParser
from paramiko import Transport, SFTPClient, SSHClient, AutoAddPolicy

REMOTE_FILE_NAME = 'theinstructor.txt'
REMOTE_COPY_NAME = 'theinstructor.stuff'

config = ConfigParser()
config.read('../EXAMPLES/sdfauth.ini')

with Transport((config['auth']['hostname'], 22)) as transport:
    transport.connect(
        username=config['auth']['username'], 
        password=config['auth']['password']
    )
    with SFTPClient.from_transport(transport) as sftp:
        sftp.put('../DATA/fruit.txt', REMOTE_FILE_NAME)

with SSHClient() as ssh:  # create paramiko client

    ssh.set_missing_host_key_policy(AutoAddPolicy())  # ignore missing keys (this is safe)

    ssh.connect(
        config['auth']['hostname'], 
        username=config['auth']['username'], 
        password=config['auth']['password'], 
    )  # connect to remote host

    ssh.exec_command(f'cp {REMOTE_FILE_NAME} {REMOTE_COPY_NAME}')

    stdin, stdout, stderr = ssh.exec_command('ls -l')
    print(stdout.read().decode())

    ssh.exec_command(f'rm {REMOTE_FILE_NAME} {REMOTE_COPY_NAME}')

    stdin, stdout, stderr = ssh.exec_command('ls -l')
    print(stdout.read().decode())

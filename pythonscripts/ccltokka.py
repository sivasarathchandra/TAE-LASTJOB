import paramiko
import xmlrunner
import logging
import sys
import datetime

username = 'kb055697'
password = 'kb055697'
hostname = 'ip15depslr.ip.devcerner.net'
command = 'ccl'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
ssh.load_system_host_keys()
ssh.connect(hostname=hostname, username=username, password=password)
transport = paramiko.Transport((hostname, 22))
transport.connect(username=username, password=password)
shell = ssh.invoke_shell()
if (shell):
    tokka = ssh.exec_command(command)
    t1 = "hostname"
    print(tokka)

import ssh

server = ssh.Connection(host='pophdevutil53', username='sc057441', private_key='Pavan#1251')
print(server)
result = server.execute('hive')
print(result)
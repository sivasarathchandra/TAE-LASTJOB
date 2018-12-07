import threading, paramiko, time, os

sshPassword = 'Pavan!1251'
sshUsername = 'SC057441'
sshServer = "pophdevutil53.northamerica.cerner.net"
oozie_cmd = 'oozie job -oozie http://pophdevutil58.northamerica.cerner.net:11000/oozie/  -info 0622975-180409134304457-oozie-oozi-C'

class ssh:
    shell = None
    client = None
    transport = None

    def __init__(self, address, username, password):
        print("Connecting to server on ip", str(address) + ".")
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)
        self.transport = paramiko.Transport((address, 22))
        self.transport.connect(username=username, password=password)

        thread = threading.Thread(target=self.process)
        thread.daemon = True
        thread.start()

    def closeConnection(self):
        if (self.client != None):
            self.client.close()
            self.transport.close()

    def openShell(self):
        self.shell = self.client.invoke_shell()

    def sendShell(self, command):
        if (self.shell):
            stdin_, stdout_, stderr_ = self.client.exec_command(command);
            stdout_.channel.recv_exit_status();
            # time.sleep(10)
            print("Oozie log Created Successfully")
            for line in stdout_.readlines():
                print(line)
        else:
            print("Shell not opened.", flush=False)

    def process(self):
        global connection
        while True:
            # Print data when available
            if self.shell != None and self.shell.recv_ready():
                alldata = self.shell.recv(1024)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(1024)
                strdata = str(alldata, "utf8")
                strdata.replace('\r', '')
                print(strdata, end="")
                if (strdata.endswith("$ ")):
                    print("\n$ ", end="")


connection = ssh(sshServer, sshUsername, sshPassword)
connection.openShell()
connection.sendShell(oozie_cmd)
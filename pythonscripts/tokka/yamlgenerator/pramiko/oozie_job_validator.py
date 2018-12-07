import unittest
import paramiko
import xmlrunner
import logging
import sys
import datetime

username = ''
password = ''
hostname = ''
command = 'ccl'

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class SimpleWidgetTestCase(unittest.TestCase):

    #setup will run first
    def setUp(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.ssh.load_system_host_keys()
        self.ssh.connect(hostname=hostname, username=username, password=password)
        self.transport = paramiko.Transport((hostname, 22))
        self.transport.connect(username=username, password=password)
        self.today = datetime.datetime.today()

    #Your test cases goes here with 'test' prefix
    def test_split(self):
        self.shell = self.ssh.invoke_shell()
        if (self.shell):
            stdin_, stdout_, stderr_ = self.ssh.exec_command(command);
            logger.info("Oozie log Created Successfully")
            for line in stdout_.readlines():
                logger.info(line)
                if self.today.strftime("%Y-%m-%d") in line:
                    self.assertIn('SUCCEEDED', line)
                    logger.info('Pipeline sucessfully passed.')
        else:
            logger.info("Shell not opened.", flush=False)


    #this will run after the test cases
    def tearDown(self):
        self.ssh.close()
        self.transport.close()


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))

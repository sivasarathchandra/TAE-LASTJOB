from tests.loggingAPI import loggingAPI
import os

class oAuthGenerator():
    """Auth function is used to get the oAuth value. As of now using auth-header-1.3.jar which will be replaced oAuth generator"""
    def Auth(self,a,x,y,z):
        oAuth=""
        s = "java -jar "+a+"auth-header-1.3.jar -k "+x+" -s "+y+" -p "+z+" > oAuthKey.txt"
        print(s)
        os.system("java -jar "+a+"auth-header-1.3.jar -k "+x+" -s "+y+" -p "+z+" > oAuthKey.txt")
        with open("oAuthKey.txt","r") as oAuthFile:
            for line in oAuthFile:
                cleanedLine = line.strip()
                if cleanedLine:  # is not empty
                    oAuth = cleanedLine
        loggingAPI.logger.info("returning oAuth Value")
        return oAuth
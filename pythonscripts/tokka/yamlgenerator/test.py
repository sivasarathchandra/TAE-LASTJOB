import sys
class A():
    def data(self,name):
        self.s = name
        print(self.s)

if __name__=="__main__":
    name=sys.argv[1]
    del sys.argv[1:]
    A().data(name)

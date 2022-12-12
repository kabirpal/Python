class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print('user defined Exception:', self.msg)
try:
    raise Accident('Crash between two buses')
except Accident as e:
    e.print_exception()
    
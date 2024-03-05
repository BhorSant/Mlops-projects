import sys

class Customeexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        pass

    def __str__(self):
        pass

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise Customeexception(e,sys)
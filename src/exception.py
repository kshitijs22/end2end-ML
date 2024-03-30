'''
To raise a custom message whenever an error occurs
'''
import sys
import logging
from src.logger import logging

def error_message_details(error,error_detail:sys):
    '''
    error - what the error message i'm getting
    error_detail: sys will tell about the exact error
    '''
    _,_,error_tb=error_detail.exc_info()
    file_name=error_tb.tb_frame.f_code.co_filename
    line_number=error_tb.tb_lineno
    error_message='Error occured in Python script [{0}] Line number [{1}] and error message [{2}]'.format
    (file_name,line_number,str(error))

    return error_message

class CustomException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


# if __name__=="__main__":
#     try:
#         a=1+'s'
#     except Exception as e:
#         logging.info(e)
#         raise CustomException(e,sys)

    
# raise CustomException("Kuch to Gadbad hai")
    

# try:
#     a=1+"s"
# except CustomException as e:
#     pass
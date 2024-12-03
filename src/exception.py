import sys 


def error_message_detail(error,error_details:str):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in python script name [{0}], line number [{1}] error massage [{2}]'.format(file_name, exc_tb.tb_lineno,str(error))

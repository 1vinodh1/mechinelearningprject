import sys
import logging

logging.basicConfig(level=logging.INFO)

def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in Python script: [{file_name}] at line [{line_number}]: {str(error)}"
    else:
        return f"Error: {str(error)}"

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message



from config import *
#!TODO: use logging module
import logging

class logger:

    def log(message_string):
        print(message_string)

    def info(*messages):
        message_str = ""
        for message in messages:
            message_str += " " + str(message)
        logger.log(message_str)
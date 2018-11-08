# from config.base import BaseConfig


class Config():
    ENVIRONMENT = "default"
    AUTOMATION_PRACTICE_URL = "https://www.baidu.com"
    AUTOMATION_PRACTICE_URL1 = "http://10.169.110.178:8088/DVWA"

class Prod():

    def __init__(self):
        print ""

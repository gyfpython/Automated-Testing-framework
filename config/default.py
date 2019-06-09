# from config.base import BaseConfig


class Config():
    ENVIRONMENT = "default"
    AUTOMATION_PRACTICE_URL = "http://localhost:8080"
    AUTOMATION_PRACTICE_URL1 = "http://localhost:8088/DVWA"

class Prod():

    def __init__(self):
        print ("")

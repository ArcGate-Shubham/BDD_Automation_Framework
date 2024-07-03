from configparser import ConfigParser

def read_configuration(categary, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(categary, key)

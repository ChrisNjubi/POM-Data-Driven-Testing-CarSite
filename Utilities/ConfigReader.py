from configparser import ConfigParser


# This method takes in the section plus the particular key to be read
# print(config.get("locators", "username"))
# print(config.get("basic info", "testsiteurl"))

#
# Create a utility function
# It accepts two parameters, section and key

def readconfig(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\config.ini")
    return config.get(section, key)


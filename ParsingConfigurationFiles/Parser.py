import configparser
data=configparser.RawConfigParser()
data.read(r"C:\Users\Admin\PycharmProjects\Python Training\ParsingConfigurationFiles\Environment.cnf")
print(data.get("QA","url"))
print(data.get("QA","username"))
print(data.get("DEV","Username"))

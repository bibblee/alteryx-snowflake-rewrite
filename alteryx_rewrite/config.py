# import snowflake.connector
# import os
# from getpass import getpass
# from configparser import ConfigParser

# config = ConfigParser()
# config.read('../config.ini')

# account = config['Snowflake']['account']
# database = config['Snowflake']['database']
# schema = config['Snowflake']['schema']
# warehouse = config['Snowflake']['warehouse']
# role = config['Snowflake']['role']

# user = getpass(prompt="UserID: ")
# password = getpass(prompt="Password: ")

# conn = snowflake.connector.connect(
#     account=account,
#     user=user,
#     password=password,
#     database=database,
#     schema=schema,
#     warehouse=warehouse,
#     role=role
# )
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM SOURCES_FOR_FUZZY ")
# results = cursor.fetchall()
# for row in results:
#     print(row)


# # cursor.close()
# # conn.close()
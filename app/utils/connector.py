# Connecting to MySQL Workbench or database
# from sqlalchemy import create_engine
import os
# from sqlalchemy.orm import sessionmaker

username = os.getenv('DATABASE_USERNAME')
password = os.getenv('DATABASE_PASSWORD')
host_url = os.getenv('DATABASE_URL')
database_name = os.getenv('DATABASE_NAME')

# connect to engine
print("connecting to MySQL Database")
# engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host_url}/{database_name}")
my_sql_string = f"mysql+mysqlconnector://{username}:{password}@{host_url}/{database_name}"
# test connection
# connection = engine.connect()
# Session = sessionmaker(bind=engine)
print(f'Connected to the MySQL Database at {host_url}')
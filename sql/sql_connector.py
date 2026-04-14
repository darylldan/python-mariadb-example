import mariadb
import sys

'''
This file creates a designated class to talk to the MariaDB interface. To avoid overloading the database
with connections, only one instance of this class should be created throughout the whole project.

Pre-requisites:
- An existing mariadb process running on the machine
- mariadb python package
'''

class MariaDBInstance():
    conn = None
    cursor: mariadb.Cursor = None

    # Initialization of the MariaDB connection, on the constructor of the class
    # host and port have default values, meaning that if left out when creating the instance of the class, the default values will be set
    def __init__(self, user: str, password: str, database: str, host: str = "127.0.0.1", port : int = 3306):
        try: 
            self.conn = mariadb.connect(
                user = user,
                password = password,
                host = host,
                port = port,
                database = database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Gets the cursor, cursors are used to execute SQL commands
        self.cursor = self.conn.cursor()

    # Cursor object getter
    def cur(self) -> mariadb.Cursor:
        return self.cursor
    
    # Closes the connection, cursor will no longer be accessible after this
    def close(self):
        self.conn.close()


    
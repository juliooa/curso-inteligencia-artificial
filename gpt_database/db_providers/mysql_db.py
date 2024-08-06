from typing import Any
from db_providers.database import BaseDatabase
import mysql.connector
from mysql.connector import Error

host_name = "localhost"
user_name = "root"
user_password = ""
db_name = "test"


class MySqlDatabase(BaseDatabase):
    def get_schema(self) -> str:
        connection = self.create_connection(
            host_name, user_name, user_password, db_name
        )
        if connection is None:
            raise Exception("Error connecting to MySQL DB")

        cursor = connection.cursor()
        cursor.execute(f"USE {db_name};")
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        schema = {}

        for table in tables:
            table_name = table[0]
            cursor.execute(f"DESCRIBE {table_name};")
            columns = cursor.fetchall()
            schema[table_name] = columns

        schema_str = ""
        for table_name, columns in schema.items():
            schema_str += f"\nTable: {table_name}\n"
            schema_str += "Columns:\n"
            for column in columns:
                schema_str += f"  {column[0]} {column[1]}\n"  # Assuming column[0] is the column name and column[1] is the column type

        return schema_str

    def query(self, sql_query: str) -> list[dict[str, Any]]:
        connection = self.create_connection(
            host_name, user_name, user_password, db_name
        )
        if connection is None:
            raise Exception("Error connecting to MySQL DB")

        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
            result = cursor.fetchall()
            if cursor.description is not None:
                column_names = [desc[0] for desc in cursor.description]

                result_dicts = [
                    {column_names[i]: value for i, value in enumerate(row)}
                    for row in result
                ]
                return result_dicts
            else:
                return []
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if connection.is_connected():
                connection.close()
        return []

    def cleanup(self):
        pass

    def create_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name, user=user_name, passwd=user_password, database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

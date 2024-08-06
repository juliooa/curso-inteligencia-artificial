import os
from typing import Any
from sqlalchemy import QueuePool, create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from db_providers.database import BaseDatabase

DB_URL = os.getenv("DATABASE_URL", "default")
engine = create_engine(DB_URL, poolclass=QueuePool, pool_size=5, max_overflow=10)
Session = sessionmaker(bind=engine)


class PostgresDatabase(BaseDatabase):
    def get_schema(self) -> str:
        engine = create_engine(DB_URL)
        inspector = inspect(engine)
        table_names = inspector.get_table_names()

        def get_column_details(table_name):
            columns = inspector.get_columns(table_name)
            return [f"{col['name']} ({col['type']})" for col in columns]

        schema_info = []
        for table_name in table_names:
            table_info = [f"Table: {table_name}"]
            table_info.append("Columns:")
            table_info.extend(
                f"  - {column}" for column in get_column_details(table_name)
            )
            schema_info.append("\n".join(table_info))

        engine.dispose()
        return "\n\n".join(schema_info)

    def query(self, sql_query: str) -> list[dict[str, Any]]:
        with Session() as session:
            statement = text(sql_query)
            result = session.execute(statement)
            return [dict(row._mapping) for row in result]

    def cleanup(self):
        engine.dispose()

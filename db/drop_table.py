# テーブル削除
import argparse
from sqlalchemy import MetaData, Table
from db.session import engine
from lib.db_constants import SCHEMA_NAME


def drop_table(table_name: str, schema: str = SCHEMA_NAME):
    metadata = MetaData(schema=schema)
    try:
        table = Table(table_name, metadata, autoload_with=engine)
        table.drop(engine)
        print(f"Dropped table: {schema}.{table_name}")
    except Exception as e:
        print(f"Failed to drop table '{schema}.{table_name}': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Drop specific table")
    parser.add_argument("table", help="The name of the table to drop")
    parser.add_argument(
        "--schema", default="skotune_ai", help="Schema name (default: skotune_ai)"
    )

    args = parser.parse_args()
    drop_table(args.table, args.schema)

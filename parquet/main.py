import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


"""
Advantages of parquet files
* possible to read only one column
"""


def write_parquet(df: pd.DataFrame, filename: str) -> None:
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)


FILENAME = 'test.parquet'

data = {
    "Languages": ["Python", "Rust", "PHP"],
    "Users": [100, 200, 3000],
    "Dynamic": [True, False, True]
}

data_frame_data = pd.DataFrame(data=data, index=list(range(1, 4)))
write_parquet(data_frame_data, FILENAME)


def read_parquet(filename: str) -> pd.DataFrame:
    table = pq.read_table(filename)
    df = table.to_pandas()
    return df


print(read_parquet(FILENAME))

def read_columns(filename: str, columns: list[str]) -> pd.DataFrame:
    table = pq.read_table(filename, columns=columns)
    return table.to_pandas()


print(read_columns(FILENAME, ["Languages"]))
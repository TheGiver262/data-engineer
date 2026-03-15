#!/usr/bin/env python
# coding: utf-8

from sys import prefix

import pandas as pd
from tqdm.auto import tqdm
from sqlalchemy import create_engine
import click


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

@click.command()
@click.option('--year', default=2021, type=int, help='Year for the data')
@click.option('--month', default=1, type=int, help='Month for the data')
@click.option('--pg_user', default='root', type=str, help='PostgreSQL username')
@click.option('--pg_pass', default='root', type=str, help='PostgreSQL password')
@click.option('--pg_host', default='localhost', type=str, help='PostgreSQL host')
@click.option('--pg_port', default='5432', type=str, help='PostgreSQL port')
@click.option('--pg_database', default='ny_taxi', type=str, help='PostgreSQL database name')
@click.option('--chunksize', default=100000, type=int, help='Chunk size for data processing')
@click.option('--target_table', default='yellow_taxi_data', type=str, help='Target table name')
def run(year, month, pg_user, pg_pass, pg_host, pg_port, pg_database, chunksize, target_table):
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'
    
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_database}')
    
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize,
    )
    first = True
    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(0).to_sql(
                name=target_table, 
                con=engine, 
                if_exists='replace'
            )
            first = False
        df_chunk.to_sql(
            name=target_table, 
            con=engine, 
            if_exists='append'
        )
    df = pd.read_csv(
        url,
        nrows=100,
        dtype=dtype,
        parse_dates=parse_dates
    )

if __name__ == '__main__':
    run()












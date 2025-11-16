# def transform():
#     print('task is tranformed')


# tasks/transform.py
import pandas as pd

def transform(**kwargs):
    """
    Transform the raw data extracted from S3:
    - Normalize column names to match database
    - Drop rows with nulls in critical columns: 'name' and 'identifier'
    """
    # Pull extracted data from XCom
    ti = kwargs['ti']
    raw_data_dict = ti.xcom_pull(key='raw_data', task_ids='extract')

    # Convert to DataFrame
    df = pd.DataFrame(raw_data_dict)

    # Map CSV columns to DB columns (case-insensitive)
    column_mapping = {
        'Name': 'name',
        'Engine': 'engine',
        'Engine Info': 'engine_info',
        'Prod Range': 'prod_range',
        'Sales Code': 'sales_code',
        'Gearbox': 'gearbox',
        'Restriction': 'restriction',
        'CHECK': 'check',
        'LINKS1-href': 'links1-href',   # Keep same as DB
        'VLOOKUP VALUE': 'vlookup_value',
        'IDENTIFIER': 'identifier',
        'KTYPE': 'ktype'
    }

    # Rename columns to match DB
    df.rename(columns=column_mapping, inplace=True)

    # Drop rows where 'name' or 'identifier' is null
    df = df[df['name'].notnull() & df['identifier'].notnull()]

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Push transformed data back to XCom for load step
    ti.xcom_push(key='transformed_data', value=df.to_dict(orient='records'))

    print("✅ Transformed data preview:")
    print(df.head())

    return "transform completed"

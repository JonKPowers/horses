## past_perf_db_structure:
This is a dict containing information used to construct tables for DRF files. The raw csv contains about 1400
columns, making it too large to contain in a single SQL database table. As a result, it needs to be split up into
multiple tables.

### Keys in dict:
  * `table_name`: name of table to be created/used in SQL database
  * `extension`: file extension of data file (i.e., [1-6] or DRF)
  * `db_fields`: dict containing name of SQL column as key and csv column as value.
    E.g.,: `'horse_name': 'horse_name'`
  * `primary_key`: list containing column to use as a primary key. Almost always ID
  * `unique_key`: list containing column names to use as the unique key for the table
  * `foreign_key`: dict containing foreign key constraint. The column name is the key, and the foreign key is the value.
     E.g.: `'horse_name': 'horses_info(horse_name)'`
import sqlite3
import table_control as tc

def add_user(user):
    dt = tc.db_connect()
    tc.create_table_user(dt)
    dt.executemany('INSERT INTO Users (firstname, lastname, company, group, tell, email, createdate, hash_key) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', user)
    dt.commit()
    tc.db_disconect(dt)

def add_group(group):
    dt = tc.db_connect()
    tc.create_table_group(dt)
    dt.executemany('INSERT INTO [Group] (name, permissions) VALUES (?, ?)', group)
    dt.commit()
    tc.db_disconect(dt)

def add_company(company):
    dt = tc.db_connect()
    tc.create_table_company(dt)
    dt.executemany('INSERT INTO Company (name, tell, email, address) VALUES (?, ?, ?, ?)', company)
    dt.commit()
    tc.db_disconect(dt)


group = ['Водитель', 1 ]
add_group(group)
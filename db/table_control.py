import sqlite3

def db_connect():
    return sqlite3.connect('../sql/peapod_db.sqlite')

def db_disconect(db):
    db.close()

def create_table_company(db):
    db.cursor()
    db.execute('''
    CREATE TABLE IF NOT EXISTS [Company] (
    id      INTEGER     PRIMARY KEY
                        UNIQUE,
    name    CHAR (255)  NOT NULL,
    tell    CHAR (255)  NOT NULL,
    email   CHAR (255)  UNIQUE
                        NOT NULL,
    address CHAR (1000) NOT NULL
    )''')

def create_table_group(db):
    db.cursor()
    db.execute('''
    CREATE TABLE IF NOT EXISTS [Group] (
    id          INTEGER    PRIMARY KEY AUTOINCREMENT
                           NOT NULL
                           UNIQUE,
    name        CHAR (255) NOT NULL
                           UNIQUE,
    permissions STRING     NOT NULL
    )''')

def create_table_user(db):
    db.cursor()
    db.execute('''
    CREATE TABLE IF NOT EXISTS [Users] (
    id         INTEGER    PRIMARY KEY AUTOINCREMENT
                          UNIQUE
                          NOT NULL,
    firstname  CHAR (255) NOT NULL,
    lastname   CHAR (255) NOT NULL,
    company    INTEGER    NOT NULL
                          REFERENCES Company (id),
    tell                  NOT NULL,
    email                 NOT NULL,
    createdate            NOT NULL
                          DEFAULT sssss,
    hash_key   CHAR (255) NOT NULL,
    [group]    INTEGER    REFERENCES [group] (id) 
                          NOT NULL
    )''')



db = db_connect()
create_table_group(db)
create_table_company(db)
create_table_user(db)
db_disconect(db)
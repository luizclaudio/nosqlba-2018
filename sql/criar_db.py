#coding: utf-8

import sqlite3

stmt = '''
    CREATE TABLE produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco REAL,
        estoque INT
    )
'''
connection = sqlite3.connect('dados.sqlite')
cursor = connection.cursor()
cursor.execute(stmt)

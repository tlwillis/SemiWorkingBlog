import sqlite3

connection = sqlite3.connect('database.db')
print ('Opened database successfully');

print ('Table created successfully');

connection.close()
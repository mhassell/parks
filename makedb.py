import sqlite3

db_file = "/media/minime/DATA/parks/parkdb.db"

conn = sqlite3.connect(db_file)

createTable = """CREATE TABLE IF NOT EXISTS parks(
 			id INTEGER PRIMARY KEY,
 			name TEXT NOT NULL,
 			latitude REAL NOT NULL,
 			longitude REAL NOT NULL,
 			state TEXT,
 			comments TEXT,
 			visited INTEGER);
			"""
c = conn.cursor()

c.execute(createTable)

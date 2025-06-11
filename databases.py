import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file) # Greitkelis (tarp programos ir duomenų bazės)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

db_kelias = r"Data\duombaze.db"

conn = create_connection(db_kelias)

# create cursor
cursor = conn.cursor() # tarsi automobilis, kuris gali vykdyti SQL komandas

cursor.execute('''CREATE TABLE IF NOT EXISTS
                users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit() # vaziuok i duombaze ir sukurk lentele

name = input("Enter your name: ") # Justas"; Drop Table Users
age = int(input("Enter your age: "))
# Insert sample data
# cursor.execute(f'Insert into Users (name, age) Values("{name}", "{age}")') # Justas"; Drop Table Users;
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name,))
conn.commit()  # Išsaugok pakeitimus

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # Gauk visus įrašus iš lentelės
print(rows) # rows yra sarašo pavidalu, kuriame yra visi įrašai kaip tuples
for row in rows:
    print(row)  # Spausdink kiekvieną įrašą
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
# Close the connection
conn.close()  # Uždaryk duomenų bazės ryšį
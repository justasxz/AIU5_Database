# import sqlite3

# def create_connection(db_file):
#     """Create a database connection to the SQLite database specified by db_file."""
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file) # Greitkelis (tarp programos ir duomenų bazės)
#         print(f"Connected to database: {db_file}")
#     except sqlite3.Error as e:
#         print(f"Error connecting to database: {e}")
#     return conn

# db_kelias = r"Data\duombaze.db"

# conn = create_connection(db_kelias)

# # create cursor
# cursor = conn.cursor() # tarsi automobilis, kuris gali vykdyti SQL komandas

# cursor.execute('''CREATE TABLE IF NOT EXISTS
#                 users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# conn.commit() # vaziuok i duombaze ir sukurk lentele

# name = input("Enter your name: ") # Justas"; Drop Table Users
# age = int(input("Enter your age: "))
# # Insert sample data
# # cursor.execute(f'Insert into Users (name, age) Values("{name}", "{age}")') # Justas"; Drop Table Users;
# # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
# # cursor.execute("INSERT INTO users (name, age) VALUES (:vardas, :amzius)", {'amzius': age,'vardas': name}) # Naudojant žodyną, kad būtų saugiau nuo SQL injekcijų

# with conn:
#     cursor.execute("INSERT INTO users (name, age) VALUES (:vardas, :amzius)", {'amzius': age,'vardas': name}) # Naudojant žodyną, kad būtų saugiau nuo SQL injekcijų
#     input("Paspausk Enter, kad įrašas būtų pridėtas...") # Palauk, kol vartotojas paspaus Enter
# # galima isivaizduoti, kad pabaigus with conn atitraukima yra padaroma conn.commit() (taip pat dalinai yra padaroma ir conn.close())
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()  # Gauk visus įrašus iš lentelės
# print(rows) # rows yra sarašo pavidalu, kuriame yra visi įrašai kaip tuples
# for row in rows:
#     print(row)  # Spausdink kiekvieną įrašą
#     print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
# # Close the connection
# conn.close()  # Uždaryk duomenų bazės ryšį

# import pandas as pd









import time
import json
import base64
import hmac
import hashlib

# Your secret key and identifiers
secret_key = "KbPeShVmYq3t6w9z$C&F)J@NcQfTjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8y/B?E"
issuer = "airtel_africa"
subject = "airtel_africa"
airtel_system_transaction_id = "12345"

# Helper for base64url encoding without padding
def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")

# Build JWT header
header = {
    "alg": "HS512",
    "typ": "JWT"
}

# Build JWT payload
now = int(time.time())
payload = {
    "jti": f"jwt-id-{now}",
    "iat": now,
    "sub": subject,
    "iss": issuer,
    "payload": {
        "txnId": airtel_system_transaction_id
    },
    "exp": now + 28800  # expires in 8 hours
}

# Encode header and payload
header_b64 = b64url(json.dumps(header, separators=(",", ":")).encode())
payload_b64 = b64url(json.dumps(payload, separators=(",", ":")).encode())
signing_input = f"{header_b64}.{payload_b64}".encode()

# Sign with HMAC-SHA512
signature = hmac.new(secret_key.encode(), signing_input, hashlib.sha512).digest()
signature_b64 = b64url(signature)

# Construct the full token
token = f"{header_b64}.{payload_b64}.{signature_b64}"

# Output the token
print(token)

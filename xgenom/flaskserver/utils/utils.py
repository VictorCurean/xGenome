import os
from hashlib import pbkdf2_hmac
from xgenom.persistence.db import db
import MySQLdb._exceptions
import jwt

def validate_user_input(input_type, **kwargs):
    if input_type == "authentication":
        if len(kwargs["username"]) <= 255 and len(kwargs["password"]) <= 255:
            return True
        else:
            return False

def generate_salt():
    salt = os.urandom(16)
    return salt.hex()


def generate_hash(plain_password, password_salt):
    password_hash = pbkdf2_hmac(
        "sha256",
        b"%b" % bytes(plain_password, "utf-8"),
        b"%b" % bytes(password_salt, "utf-8"),
        10000,
    )
    return password_hash.hex()

def db_write(query, params):
    try:
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        cursor.close()

        return True

    except MySQLdb._exceptions.IntegrityError:
        cursor.close()
        return False

def db_read(query, params=None):
    cursor = db.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    entries = cursor.fetchall()
    cursor.close()

    content = []

    for entry in entries:
        content.append(entry)

    return content

JWT_SECRET_KEY="CSUBBSecretKey"

def generate_jwt_token(content):
    encoded_content = jwt.encode(content, JWT_SECRET_KEY, algorithm="HS256")
    token = str(encoded_content).split("'")[1]
    return token

def validate_user(username, password):
    current_user = db_read("""SELECT * FROM users_auth WHERE username = %s""", (username,))

    if len(current_user) == 1:
        saved_password_hash = current_user[0][3]
        saved_password_salt = current_user[0][2]
        password_hash = generate_hash(password, saved_password_salt)

        if password_hash == saved_password_hash:
            user_id = current_user[0][0]
            jwt_token = generate_jwt_token({"id": user_id})
            return jwt_token
        else:
            return False

    else:
        return False

def persist_token(username, jwt):
    cursor = db.cursor()
    sql = "UPDATE users_auth SET token = %s WHERE username = %s"
    val = (jwt, username)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()


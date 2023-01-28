from werkzeug.security import check_password_hash, generate_password_hash


def hash_password(password: str) -> str:
    return generate_password_hash(password=password)


def check_password(password: str, hashed_password: str) -> bool:
    return check_password_hash(pwhash=hashed_password, password=password)

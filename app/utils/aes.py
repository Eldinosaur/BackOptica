import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64

# Leer claves del entorno
SECRET_KEY = os.getenv("AES_SECRET_KEY")
IV = os.getenv("AES_IV")

if SECRET_KEY is None or IV is None:
    raise ValueError("Faltan las variables AES_SECRET_KEY o AES_IV en el entorno.")

SECRET_KEY = SECRET_KEY.encode()
IV = IV.encode()

def encrypt(plain_text: str) -> str:
    backend = default_backend()
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(IV), backend=backend)
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plain_text.encode()) + padder.finalize()

    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(encrypted).decode()

def decrypt(encrypted_text: str) -> str:
    backend = default_backend()
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(IV), backend=backend)
    decryptor = cipher.decryptor()

    encrypted_data = base64.b64decode(encrypted_text)
    decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
    return decrypted.decode()

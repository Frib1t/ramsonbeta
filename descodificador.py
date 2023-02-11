import hashlib
import os
import shutil

HASH = "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"


def hash_password(password):
    # Genera un hash a partir de la contraseña
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash


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


def main():
    pregunta = input("Desea desencriptar: [S/N] ")
    if pregunta == "S":
        password2 = input("Ingrese la contraseña: ")
        hash2 = hash_password(password2)
        directory = input("Ingrese la ruta del directorio a desencriptar: ")
        attempt = 1
        while attempt <= 3:
            # Intenta descifrar el directorio
            if hash2 == HASH:
                decrypt_directory(directory, password2)
                print("El directorio ha sido descifrado.")
                break
            else:
                # Si la contraseña es incorrecta, incrementa el contador de intentos
                attempt += 1
                if attempt > 3:
                    # Si se han realizado 3 intentos fallidos, elimina el directorio
                    print("Ha alcanzado el número máximo de intentos. Eliminando el directorio...")
                    shutil.rmtree(directory)
                    break
                else:
                    print("Contraseña incorrecta. Intento número", attempt)
                    password = input("Ingrese la contraseña: ")
    else:
        exit()


if __name__ == '__main__':
    main()

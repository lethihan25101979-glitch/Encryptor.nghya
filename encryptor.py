import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

print(",--.    ,-----.      ,--.,--.      ,---.  ,------. ,--.")
print("|  |   '  .-.  '     |  ||  |     /  O  \ |  .--. '|  |  ___________")
print("|  |   |  | |  |,--. |  ||  |    |  .-.  ||  '--' ||  | | encryptor |")
print("|  '--.'  '-'  '|  '-'  /|  |    |  | |  ||  | --' |  | '-----------'")
print("`-----' `-----'  `-----' `--'    `--' `--'`--'     `--'   -nghya-")

# khóa
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

def encrypt_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    nonce = os.urandom(12)
    encrypted_data = aesgcm.encrypt(nonce, data, None)

    # Lấy ext
    ext = os.path.splitext(input_file)[1].encode()

    # Se
    with open(output_file, 'wb') as f:
        f.write(nonce + bytes([len(ext)]) + ext + encrypted_data)

if __name__ == "__main__":
    input_file = input("Fill your file name: ")
    encrypt_file(input_file, "encrypted")
    print("Encryption completed, file saved as 'encrypted'")
    # Lưu khóa ra file để dùng cho giải mã
    with open("key.bin", "wb") as f:
        f.write(key)
    print("Key has been saved to 'key.bin' for decryption")

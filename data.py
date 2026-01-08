from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

data = "d1dd8bcf29" 

data_bytes = bytes.fromhex(data)

cipher = AES.new(key, AES.MODE_CBC, iv)

padded_data = pad(data_bytes, AES.block_size)

encrypted_data = cipher.encrypt(padded_data)

encrypted_data_hex = binascii.hexlify(encrypted_data).decode()

print(f"Encrypted data: {encrypted_data_hex}")

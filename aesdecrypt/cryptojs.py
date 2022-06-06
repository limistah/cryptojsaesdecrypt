import base64
from hashlib import md5
from Crypto.Cipher import AES

BLOCK_SIZE = 16

pad = lambda s: str(s) + (BLOCK_SIZE - len(str(s)) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(str(s)) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def bytes_to_key(data, salt, output=48):
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    final_key = key
    while len(final_key) < output:
        key = md5(key + data).digest()
        final_key += key
    return final_key[:output]

def decryptCipher(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted)
    assert encrypted[0:8] == b"Salted__"
    salt = encrypted[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32+16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encrypted[16:])).decode()


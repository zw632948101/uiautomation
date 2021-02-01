try:
    from crypto.Cipher import AES
except ModuleNotFoundError:
    from Crypto.Cipher import AES
from binascii import a2b_hex
from os import getenv
import json

def decrypt(cipher, mode=AES.MODE_CBC):
    plain_text = AES.new(key=getenv('INTERFACE_KEY'),
                         mode=mode,
                         IV='Wv1rN6#cv5Zwl8Tc').decrypt(a2b_hex(cipher))
    try:
        return json.loads(bytes.decode(plain_text).rstrip('\0'))
    except json.decoder.JSONDecodeError as e:
        return bytes.decode(plain_text).rstrip('\0')
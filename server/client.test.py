import rsa
import rsa.randnum
from Crypto.Cipher import AES

pubkey, privkey = rsa.newkeys(256)

aes_key = "7dfd5fc9832f32c210c4ba68fadaf76f"
aes_key = bytes.fromhex(aes_key)

# print("pubkey: ", pubkey.save_pkcs1())
# print("privkey: ", privkey.save_pkcs1())

image = open("Green.png", "rb").read()

# print(image.hex())
def encrypt(data):
    """Encrypts the message"""
    cipher = AES.new(aes_key, AES.MODE_EAX)
    cipheredData, tag = cipher.encrypt_and_digest(data)
    return (cipheredData,tag,cipher.nonce)

cipheredData, tag, nonce = encrypt(image)
# print("cipheredData: ", cipheredData.hex())
# print("tag: ", tag.hex())
# print("nonce: ", nonce.hex())
pb ="""-----BEGIN RSA PUBLIC KEY-----
MCgCIQCIyuJpa2hb+abTQnVV8z2M1BTWROHK3DNxtiJ4dpl+7QIDAQAB
-----END RSA PUBLIC KEY-----"""
pb = rsa.PublicKey.load_pkcs1(pb.encode("utf-8"))
pb =pb._save_pkcs1_der()
pb = pb.hex()
print("pbke",pb)

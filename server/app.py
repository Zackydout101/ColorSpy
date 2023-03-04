from flask import Flask, request, jsonify
import rsa
import rsa.randnum
from Crypto.Cipher import AES

app = Flask(__name__)

# Generate the Encryption Keys
(pubkey, privkey) = rsa.newkeys(256)
aes_key = rsa.randnum.read_random_bits(16)
aes_pubkey = rsa.encrypt(aes_key, pubkey) # Encrypt the AES key with the RSA public key

@app.route("/")
def hello_world():
    return "<p>Welcome to our Api</p>"

@app.route("/key")
def get_public_key():
    """Sends the encrypted AES key to the client"""
    return aes_pubkey

@app.route("/process",methods=["POST"])
def process_image():
    image = request.files["image"].stream.read()
    tag = request.form["tag"]

    # Decrypt the data
    data = decrypt(data,tag)
    return jsonify({"message":"success"})

def encrypt(data):
    """Encrypts the message"""
    cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return (ciphertext,tag)

def decrypt(data,tag):
    """Decrypts the message"""
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    decrypted = cipher_aes.decrypt_and_verify(data, tag)

    return decrypted

from flask import Flask, request, jsonify
import rsa
import rsa.randnum
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from model import detectColor 
# from Crypto.PublicKey import RSA
import io

app = Flask(__name__)

# Generate the Encryption Keys
(pubkey, privkey) = rsa.newkeys(512)
aes_key = get_random_bytes(16)


@app.route("/")
def hello_world():
    return "<p>Welcome to our Api</p>"

@app.route("/key",methods=["POST"])
def get_public_key():
    """Sends the encrypted AES key to the client"""
    # Get the client's public key in hex
    client_pubkey= request.form["key"]
    print(client_pubkey)
    #convert the public key from hex to bytes
    client_pubkey = bytes.fromhex(client_pubkey)
    client_pubkey = io.BytesIO(client_pubkey)
    print(client_pubkey)
    #convert to publickey object
    client_pubkey = RSA.import_key(client_pubkey)
    # print(client_pubkey) 

    # # Encrypt the server's AES key with the client's RSA public key so that only the client can decrypt it
    # aes_pubkey = rsa.encrypt(aes_key, client_pubkey)#.decode("utf-8",errors="ignore") # Encrypt the AES key with the RSA public key

    return jsonify({"pubkey":pubkey.save_pkcs1().decode("utf-8"),"aes_pubkey":aes_pubkey.hex()})

@app.route("/process",methods=["POST"])
def process_image():
    image =request.form["image"]
    image = bytes.fromhex(image)
    # image = io.BytesIO(image)

    tag = request.form["tag"]
    tag = bytes.fromhex(tag)
    
    nonce = request.form["nonce"]
    nonce = bytes.fromhex(nonce)
    
    pubKey = request.form["key"]
   
    # Decrypt the image
    image = decrypt(image,tag,nonce)

    # Detect the color of the image
    color = detectColor(image)

    return jsonify({"color":color})

@app.route("/test",methods=["GET"])
def test():
    image = open("Green.png", "rb").read()
    print(image)

    cipheredData, tag, nonce = encrypt(image)
    # print("1.Original image", image.hex())
    # print("2. Encrypted: ", cipheredData.hex())
    image =decrypt(cipheredData,tag,nonce)
    print("3. decrypted", image)

    # print("pubkey: ", pubkey.save_pkcs1().decode("utf-8"))
    # print ("AesKEy:",aes_key.hex())

    return detectColor(image)

def encrypt(data):
    """Encrypts the message"""
    cipher = AES.new(aes_key, AES.MODE_EAX)
    cipheredData, tag = cipher.encrypt_and_digest(data)
    return (cipheredData,tag,cipher.nonce)

def decrypt(data,tag,nonce):
    """Decrypts the message"""
    cipher_aes = AES.new(aes_key, AES.MODE_EAX,nonce =nonce)
    decrypted = cipher_aes.decrypt(data)

    return decrypted
    # return "hello"
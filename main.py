import base64
import time

def encode():
   text = input("What do you want to encode? ==>")
   text_bytes = text.encode('utf-8')
   encoded = base64.b64encode(text_bytes) 
   encoded_str = encoded.decode('utf-8') 
   print(encoded_str)
   with open("output.txt", "w") as file:
      file.write(f"\nYou chose to encode \ninput = {text} \noutput = {encoded_str} \n----------------")
   print("saved to output.txt")

def decode():
   text = input("What do you want to decode? ==>")
   text_bytes = text.encode('utf-8')  
   decoded = base64.b64decode(text_bytes) 
   decoded_str = decoded.decode('utf-8')
   print(decoded_str)
   with open("output.txt", "w") as file:
      file.write(f"\nYou chose to decode \ninput = {text} \noutput = {decoded_str} \n----------------")
   print("saved to output.txt")


print("Base64 encoder/decoder")

time.sleep(1)

choice = input("""Do you want to encode or decode?
1 = encode
2 = decode
choice: """)

if choice == "1":
   encode()
   time.sleep(10)

if choice == "2":
   decode()
   time.sleep(10)

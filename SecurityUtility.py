import random 
import base64
class SecurityUtility:
    """security model and class"""
    ENCRYPT_KEY="@#$<<i m not gonna tell you my key though>!@>"
    
    def _init_(self):
        print("constructor of security class")

    def encode(self,string):
        encoded_chars = []
        for i in range(len(string)):
            key_c = self.ENCRYPT_KEY[i % len(self.ENCRYPT_KEY)]
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = "".join(encoded_chars)
        return base64.urlsafe_b64encode(encoded_string)

    def decode(self,string):
        decoded_chars = []
        string = base64.urlsafe_b64decode(string)
        for i in range(len(string)):
            key_c = self.ENCRYPT_KEY[i % len(self.ENCRYPT_KEY)]
            encoded_c = chr(abs(ord(string[i]) - ord(key_c) % 256))
            decoded_chars.append(encoded_c)
        decoded_string = "".join(decoded_chars)
        return decoded_string
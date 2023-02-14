from cryptography.fernet import Fernet
import environ
import os
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# env = environ.Env(DEBUG=(bool, True))
# environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))
# key = env('FERNET_KEY')
# fernet = Fernet(key)


    
# def json_record(extra):
    
#     encrypt_str = fernet.encrypt(f"{extra}".encode('ascii'))
#     return encrypt_str



# def record_json(encrypt_str): 

    
#     fernet = Fernet(key)
#     decrypt_str = fernet.decrypt(encrypt_str)
#     return decrypt_str
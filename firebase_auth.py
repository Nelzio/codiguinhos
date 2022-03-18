from pprint import pprint
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
import os
# from zambezi.settings import BASE_DIR
import json
from decouple import config

# cred_json = os.path.join(BASE_DIR, "firebaseSDK.json")
cred_json = json.loads(config('FIREBASE_SDK_KEYS'))
cred = credentials.Certificate(cred_json)
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()
# auth_db = auth

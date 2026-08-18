"""
firebase_config.py

Initializes the Firebase Admin SDK using a local service-account key file
and exposes a Firestore client (`db`) for the rest of the app to use.

Local development only:
- firebase-key.json must sit next to this file.
- Never commit firebase-key.json to version control.
- Never send its contents to the frontend or to Gemini.
"""
import os
import firebase_admin
from firebase_admin import credentials, firestore

db = None

try:
    key_path = os.environ.get("FIREBASE_KEY")

    if not key_path:
        raise Exception("FIREBASE_KEY environment variable not found")

    cred = credentials.Certificate(key_path)
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    print("✅ Firebase Connected Successfully")

except Exception as e:
    print(f"❌ Firebase Error: {e}")

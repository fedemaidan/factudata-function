
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Inicializar la aplicación de Firebase
cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred)

def update_firebase_data(id, row):
    db = firestore.client()
    doc_ref = db.collection('facturas').document(id)
    doc_ref.update(row)

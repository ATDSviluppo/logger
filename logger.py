from flask import Flask, request
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Carica le variabili dal file .env
load_dotenv()

app = Flask(__name__)

# Leggi le variabili di configurazione dal file .env
PORT = int(os.getenv('PORT', 5000))
LOG_PATH = os.getenv('LOG_PATH', 'logs/')
LOG_NAME = os.getenv('LOG_NAME', 'log')

@app.route('/log', methods=['POST'])
def log_json():
    data = request.get_json()
    if not data:
        return 'Nessun dato JSON ricevuto', 400

    # Ottieni la data e l'ora corrente
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    # Costruisci il nome completo del file
    filename = f'{LOG_NAME}_{timestamp}.json'
    filepath = os.path.join(LOG_PATH, filename)

    # Crea la directory se non esiste
    os.makedirs(LOG_PATH, exist_ok=True)

    # Salva i dati JSON nel file
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

    print(f'Dati salvati nel file {filepath}')

    return f'Dati salvati nel file {filepath}', 200

if __name__ == '__main__':
    app.run(debug=True, port=PORT)


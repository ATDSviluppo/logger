#!/bin/bash

# Verifica se 'pip' è installato
if ! command -v pip &> /dev/null
then
    echo "pip non è installato. Per favore installalo prima di procedere."
    exit 1
fi

# Definisci le dipendenze richieste
REQUIRED_PKG=("flask" "python-dotenv")

# Installa le dipendenze mancanti
for PKG in "${REQUIRED_PKG[@]}"; do
    if ! pip show $PKG &> /dev/null; then
        echo "Il pacchetto $PKG non è installato. Installazione in corso..."
        pip install $PKG
    else
        echo "Il pacchetto $PKG è già installato."
    fi
done

# Verifica se il file .env esiste, altrimenti crea uno di esempio
if [ ! -f ".env" ]; then
    echo "Il file .env non esiste. Creazione di un file .env di esempio..."
    cat <<EOL > .env
PORT=5000
LOG_PATH=logs/
LOG_NAME=log
EOL
    echo "File .env creato con valori predefiniti."
fi

# Avvia l'applicazione Python
echo "Avvio dell'applicazione..."
python logger.py


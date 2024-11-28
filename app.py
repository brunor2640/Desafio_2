from flask import Flask, request, jsonify, render_template
import os
import json
from datetime import datetime

app = Flask(__name__)

# Configuração da pasta de dados
DATA_FOLDER = 'data'

# Função para carregar dados de um arquivo JSON
def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Erro ao carregar JSON: {e}")
        return None

# Função para processar guest checks
def process_guest_checks(response):
    guest_checks = response.get("guestChecks", [])
    for check in guest_checks:
        taxation = check.get("taxation", [])
        print(f"Processing taxation for guest check {check['guestCheckId']}: {taxation}")

# Função para formatar a data no formato 'YYYY-MM-DD'
def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError as e:
        print(f"Erro na formatação da data: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    store_id = request.args.get('store_id')
    bus_dt = request.args.get('bus_dt')
    data_type = request.args.get('data_type')

    # Formatar a data corretamente
    formatted_date = format_date(bus_dt)
    if not formatted_date:
        return jsonify({"error": "Invalid date format"}), 400

    # Construindo o caminho do arquivo
    file_path = os.path.join(DATA_FOLDER, data_type, formatted_date[:4], formatted_date[5:7], f"{formatted_date}_storeId_{store_id}.json")
    print(f"File path: {file_path}")  # Para fins de depuração

    # Verificar a existência do arquivo e carregar os dados
    if os.path.exists(file_path):
        data = load_json(file_path)
        if data:
            if data_type == 'guest_checks':
                process_guest_checks(data)
            return jsonify(data)
        else:
            return jsonify({"error": "Error loading JSON data"}), 500
    else:
        return jsonify({"error": "Data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


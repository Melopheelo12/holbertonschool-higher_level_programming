import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Fonctions de lecture de données ---

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Cette ligne permet d'accéder aux colonnes par leur nom (ex: row['name'])
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        # On convertit les objets Row en dictionnaires classiques
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

# --- Route principale ---

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    # 1. Sélection de la source
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # 2. Filtrage par ID (Identique à la tâche 3)
    if product_id:
        try:
            target_id = int(product_id)
            products = [p for p in products if p['id'] == target_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID format"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
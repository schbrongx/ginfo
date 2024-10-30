from flask import Flask, jsonify, request, render_template
import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        host="db_master",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locations', methods=['POST'])
def add_location():
    data = request.get_json()
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO locations (name, geom) VALUES (%s, ST_GeomFromText(%s, 4326))", (data['name'], data['geom']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Location added!"}), 201

@app.route('/locations', methods=['GET'])
def get_locations():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT name, ST_AsText(geom) FROM locations")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)


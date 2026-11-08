from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

@app.route("/api/message")
def message():
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST", "mysql"),
            user=os.getenv("DB_USER", "appuser"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "appdb")
        )

        cursor = db.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()

        cursor.close()
        db.close()

        return jsonify({
            "message": "Three-tier application is running!",
            "database": "Connected successfully"
        })

    except Exception as error:
        return jsonify({
            "message": "Backend is running",
            "database": "Connection unavailable"
        }), 503

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

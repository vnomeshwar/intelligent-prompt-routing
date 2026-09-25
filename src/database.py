import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "prompt_routing.db"

def get_connection():
    return sqlite3.connect(DB)

def initialize_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS routed_prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL,
            category TEXT NOT NULL,
            sentiment TEXT,
            route TEXT NOT NULL,
            confidence REAL,
            method TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()

def save_result(result):
    with get_connection() as conn:
        conn.execute("""
        INSERT INTO routed_prompts
        (prompt, category, sentiment, route, confidence, method)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            result["prompt"], result["category"], result.get("sentiment"),
            result["route"], result["confidence"], result["method"]
        ))
        conn.commit()

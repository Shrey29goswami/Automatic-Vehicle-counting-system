import json
import os
from datetime import datetime

HISTORY_FILE = "data/history.json"

def save_history(filename):
    os.makedirs("data", exist_ok=True)

    data = []

    # ✅ SAFE LOAD
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                content = f.read().strip()
                if content:  # only load if not empty
                    data = json.loads(content)
        except:
            data = []  # fallback if corrupted

    data.append({
        "file": filename,
        "time": str(datetime.now())
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except:
        return []
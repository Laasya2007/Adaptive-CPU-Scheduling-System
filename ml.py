import json
import os

FILE = "history.json"

history = []

if os.path.exists(FILE):
    try:
        with open(FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

def save():
    with open(FILE, "w") as f:
        json.dump(history, f)

def predict(bt):
    if len(history) == 0:
        return sum(bt) / len(bt)
    total = sum([h["avg_bt"] for h in history])
    return total / len(history)

def store(avg_bt, decision):
    history.append({
        "run": len(history) + 1,
        "avg_bt": avg_bt,
        "decision": decision
    })
    save()

def clear():
    global history
    history = []
    save()
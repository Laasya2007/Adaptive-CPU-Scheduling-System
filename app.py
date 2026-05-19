from flask import Flask, request, jsonify, render_template
import ml
import statistics

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# ================= RUN =================
@app.route("/run", methods=["POST"])
def run():
    try:
        data = request.get_json()
        bt = data.get("bt", [])

        if not bt:
            return jsonify({"error": "No processes provided"})

        bt = [int(x) for x in bt]

        avg_bt = sum(bt) / len(bt)
        variance = statistics.variance(bt) if len(bt) > 1 else 0

        # Decision
        if variance < 5:
            decision = "Round Robin (similar workload)"
        elif variance < 50:
            decision = "Adaptive Hybrid"
        else:
            decision = "SJF (high variation)"

        wt = round(avg_bt / 2, 2)
        tat = round(avg_bt + wt, 2)

        prediction = ml.predict(bt)
        ml.store(avg_bt, decision)

        output = "=== Adaptive Hybrid Scheduling ===\n"
        output += "Gantt Chart:\n| "
        for i in range(len(bt)):
            output += f"P{i+1} | "
        output += f"\nAverage WT = {wt}\nAverage TAT = {tat}"

        return jsonify({
            "output": output,
            "wt": wt,
            "tat": tat,
            "decision": decision,
            "variance": round(variance, 2),
            "prediction": round(prediction, 2),
            "history": ml.history
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": "Backend crashed"})

# ================= RESET (UI ONLY) =================
@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({"msg": "UI reset only"})

# ================= CLEAR ML =================
@app.route("/clear", methods=["POST"])
def clear():
    ml.clear()
    return jsonify({"msg": "history cleared"})

# ================= MAIN =================
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
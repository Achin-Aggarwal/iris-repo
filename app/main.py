from flask import Flask, jsonify

app = Flask(__name__)

# ✅ Health check endpoint (used by Kubernetes)
@app.route("/health")
def health():
    return jsonify(status="ok"), 200

# ✅ Test endpoint for verification
@app.route("/iris")
def iris():
    return jsonify(message="IRIS API is alive!"), 200

# ✅ Optional root route
@app.route("/")
def home():
    return jsonify(message="Welcome to IRIS API"), 200

if __name__ == "__main__":
    # Bind to all interfaces (Kubernetes needs 0.0.0.0)
    app.run(host="0.0.0.0", port=8080)

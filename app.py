import os
from flask import Flask, redirect, render_template, request, jsonify
from flask_cors import CORS
import logging
from datetime import datetime

app = Flask(__name__)
CORS(app)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ─── Configuration ───────────────────────────────────────────
CHARIOW_URL = "https://xenniebt.mychariow.shop/prd_ovnmq5"
EBOOK_TITLE = "E-Commerce & Dropshipping Masterclass"
AUTHOR      = "TCHEKPELE Koboyo Méric"


# ─── Routes ──────────────────────────────────────────────────

@app.route("/")
def landing():
    return render_template("index.html",
                           title=EBOOK_TITLE,
                           author=AUTHOR)


@app.route("/acheter")
def acheter():
    ip     = request.headers.get("X-Forwarded-For", request.remote_addr)
    source = request.args.get("source", "direct")
    ts     = datetime.utcnow().isoformat()
    logger.info(f"[CLIC] ts={ts} | ip={ip} | source={source}")
    return redirect(CHARIOW_URL, code=302)


@app.route("/api/stats")
def stats():
    return jsonify({
        "status": "ok",
        "ebook": EBOOK_TITLE,
        "author": AUTHOR,
        "chariow": CHARIOW_URL,
        "timestamp": datetime.utcnow().isoformat()
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


# ─── Lancement ───────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
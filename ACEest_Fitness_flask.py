from flask import Flask, jsonify, request, abort
import os
from uuid import uuid4

def create_app():
    app = Flask(__name__)
    app.config['WORKOUTS'] = []

    @app.route("/")
    def index():
        return jsonify({
            "app": "ACEest Fitness & Gym",
            "description": "Workout tracking API",
            "endpoints": ["/workouts", "/health", "/version"]
        })

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.route("/version")
    def version():
        return jsonify({"version": os.getenv("APP_VERSION", "v1.0.0")})

    @app.route("/workouts", methods=["GET"])
    def list_workouts():
        return jsonify(app.config['WORKOUTS'])

    @app.route("/workouts", methods=["POST"])
    def add_workout():
        payload = request.get_json(force=True, silent=True)
        if not payload:
            abort(400, "JSON body required")
        if "workout" not in payload or "duration" not in payload:
            abort(400, "Missing fields")
        item = {"id": str(uuid4()), "workout": payload["workout"], "duration": int(payload["duration"])}
        app.config['WORKOUTS'].append(item)
        return jsonify(item), 201

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

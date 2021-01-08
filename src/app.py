from flask import Flask, request, jsonify


app = Flask(__name__)


# Running the application on default host (localhost) and default port 5000
if __name__ == "__main__":
    app.run()
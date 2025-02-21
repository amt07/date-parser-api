from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Welcome to the Date Parser API! Use /parse-date?date=23 Sep to parse a date."

# Date Parsing Route
@app.route('/parse-date', methods=['GET'])
def parse_date():
    date_str = request.args.get('date', '')

    try:
        full_date_str = f"{date_str} 2024"  # Append the current year
        parsed_date = datetime.strptime(full_date_str, "%d %b %Y")
        formatted_date = parsed_date.strftime("%Y-%m-%dT00:00:00Z")

        return jsonify({"parsed_date": formatted_date})

    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

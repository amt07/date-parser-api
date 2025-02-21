from flask import Flask, request, jsonify
import dateparser
import pytz

app = Flask(__name__)

@app.route('/parse-date', methods=['GET'])
def parse_date():
    date_text = request.args.get('date')

    if not date_text:
        return jsonify({"error": "No date provided"}), 400

    # Parse date & time with timezone support
    parsed_date = dateparser.parse(
        date_text,
        settings={'TIMEZONE': 'UTC', 'TO_TIMEZONE': 'Asia/Kolkata', 'PREFER_DATES_FROM': 'future'}
    )

    if parsed_date:
        # Format outputs for different use cases
        formatted_iso = parsed_date.isoformat()  # ISO 8601 format
        formatted_12hr = parsed_date.strftime('%Y-%m-%d %I:%M %p %Z')  # 12-hour format
        formatted_24hr = parsed_date.strftime('%Y-%m-%d %H:%M %Z')  # 24-hour format

        return jsonify({
            "parsed_date_iso": formatted_iso,
            "formatted_12hr": formatted_12hr,
            "formatted_24hr": formatted_24hr
        })
    else:
        return jsonify({"error": "Invalid date format"}), 400

if __name__ == '__main__':
    app.run(debug=True)

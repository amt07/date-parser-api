from flask import Flask, request, jsonify
import dateparser
from datetime import datetime, time
import os

app = Flask(__name__)

@app.route('/parse-date', methods=['GET'])
def parse_date():
    date_text = request.args.get('date')

    if not date_text:
        return jsonify({"error": "No date provided"}), 400

    # Enable relative date parsing
    parsed_date = dateparser.parse(
        date_text,
        settings={
            'RELATIVE_BASE': datetime.now(),  
            'PREFER_DATES_FROM': 'future',    
            'PARSERS': ['relative-time', 'absolute-time'],  
        }
    )

    if parsed_date:
        # Default to 12:00 PM if no time is provided
        if parsed_date.time() == time(0, 0):  
            parsed_date = parsed_date.replace(hour=12, minute=0)

        return jsonify({
            "parsed_date_iso": parsed_date.isoformat(),
            "formatted_12hr": parsed_date.strftime('%Y-%m-%d %I:%M %p'),
            "formatted_24hr": parsed_date.strftime('%Y-%m-%d %H:%M')
        })
    else:
        return jsonify({"error": "Invalid date format"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get PORT from environment
    app.run(host="0.0.0.0", port=port, debug=True)

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Directly paste your AbuseIPDB API key here
ABUSEIPDB_API_KEY = "57bb55ef7b453c380f5af6770af57240440780bd6e99a6ec0594f8d0ac74e09197e39d8fca01cfbf"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    try:
        ip_or_domain = request.form["query"]

        headers = {
            "Key": ABUSEIPDB_API_KEY,
            "Accept": "application/json"
        }

        params = {
            "ipAddress": ip_or_domain,
            "maxAgeInDays": 90
        }

        response = requests.get("https://api.abuseipdb.com/api/v2/check", headers=headers, params=params)
        data = response.json()

        if "data" in data:
            score = data["data"].get("abuseConfidenceScore", 0)
            if score >= 75:
                risk = "❌ Dangerous"
            elif score >= 50:
                risk = "🚨 Suspicious"
            elif score >= 25:
                risk = "⚠️ Low Risk"
            else:
                risk = "✅ Safe"

            result = {
                "ipAddress": data["data"].get("ipAddress", "N/A"),
                "domain": data["data"].get("domain", "N/A"),
                "abuseConfidenceScore": score,
                "riskLevel": risk,
                "countryCode": data["data"].get("countryCode", "N/A"),
                "isp": data["data"].get("isp", "N/A"),
                "totalReports": data["data"].get("totalReports", 0),
                "usageType": data["data"].get("usageType", "N/A"),
                "lastReportedAt": data["data"].get("lastReportedAt", "Never"),
            }
            return jsonify(result)
        else:
            return jsonify({"error": "No result found."}), 404

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

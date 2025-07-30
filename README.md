# 🔎 Cyber Threat Intelligence Dashboard

A beginner-friendly web application to check the **risk level of IP addresses** using the **AbuseIPDB** API.

---

## 🌐 Live Features

* Input any **domain/IP**
* Fetch threat intelligence from **AbuseIPDB**
* Automatically categorize IPs as:

  * � Safe
  * 🟢 Low Risk
  * 🟡 Suspicious
  * 🔴 Dangerous
* Risk level shown in a clean, modern UI

---

## 📂 Project Structure

```
cti-dashboard/
│
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # HTML UI
├── static/
│   └── style.css        # Styling
└── README.md            # Project overview
```

---

## 🛠️ Tech Stack

* Python + Flask
* HTML + CSS + JavaScript
* AbuseIPDB API

---

## 🔐 Setup Instructions

### 📁 Clone the Repo

```bash
git clone https://github.com/yourusername/cti-dashboard.git
cd cti-dashboard
```

### ⚙️ Install Dependencies

```bash
pip install flask requests
```

### 🔑 Insert Your API Key (directly in `app.py`)

1. Get your free API key from [AbuseIPDB](https://www.abuseipdb.com/register)
2. Paste it inside `app.py` as:

```python
ABUSE_API_KEY = "your_api_key_here"
```

### 🚀 Run the App

```bash
python app.py
```

Visit `http://localhost:5000`

---

## 🔍 Sample Results

| IP Address       | Risk Level    | Reports |
| ---------------- | ------------- | ------- |
| `8.8.8.8`        | 🌿 Safe       | 0       |
| `45.155.204.151` | 🟡 Suspicious | 10+     |

---

## 🌟 Credits

Built by **Kamlesh** as a beginner-friendly Cybersecurity project.

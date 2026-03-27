# ✈️ VoyageAI – Intelligent Trip Planner

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![CrewAI](https://img.shields.io/badge/CrewAI-Agentic-green)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![Tavily](https://img.shields.io/badge/Tavily-Search-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Overview

VoyageAI is an **AI-powered Trip Planner** built using:

- 🤖 CrewAI (Agentic AI)
- 🧠 Groq (Llama 3 LLM)
- 🌐 Tavily (Web Search)
- 🎨 Streamlit (UI)

It generates a **complete travel plan** including:

- 🌤 Weather
- 💰 Budget
- 📍 Top Places
- 🏨 Hotels
- 🗓️ Day-wise Itinerary
- 🚗 Travel Tips
- 💱 Currency Conversion

---

## 📸 Demo UI

> Add your screenshots here

---

## ✨ Features

- Multi-agent architecture (CrewAI)
- Real-time search via Tavily
- LLM-powered planning (Groq)
- Smart budget estimation (local + USD)
- Structured itinerary generation
- Clean Streamlit UI
- Currency converter

---

## 🏗️ Project Structure

```text
trip_planner_agent/
│
├── .env
├── pyproject.toml
├── README.md
│
└── src/
    └── trip_planner_agent/
        │
        ├── main.py
        ├── crew.py
        │
        ├── config/
        │   ├── agents.yaml
        │   └── tasks.yaml
        │
        └── tools/
            ├── tavily_tool.py
            └── currency_tool.py
```

---

## ⚙️ Installation (Using UV)

### 1️⃣ Install uv

```bash
pip install uv
```

### 2️⃣ Create Virtual Environment

```bash
uv venv
```

Activate:

```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
EXCHANGE_RATE_API_KEY=your_exchange_api_key
```

---

## ▶️ Run the App

```bash
streamlit run src/trip_planner_agent/main.py
```

App URL:

```text
http://localhost:8501
```

---

## 🧠 How It Works

### 🔹 Agents

#### 1. Intent Mapper

Extracts:
- destination
- budget
- preferences

#### 2. Researcher

Uses Tavily to fetch:
- weather
- attractions
- costs

#### 3. Planner

Generates:
- weather
- budget
- places
- hotels
- itinerary
- travel tips

---

## 📊 Example Output

```text
Weather:
Temperature: 15°C
Condition: Pleasant

Budget:
Stay: ₹30,000 (~$400)
Food: ₹1,200/day

Places:
1. Sensoji Temple
2. Tokyo Skytree

Itinerary:
Day 1:
Morning - Visit temple
Afternoon - Explore city
Evening - Dinner
```

---

## 💱 Currency Converter

Supports:
- INR
- USD
- JPY
- EUR

---

## 🛠️ Tech Stack

- Frontend → Streamlit
- Backend → CrewAI
- LLM → Groq (Llama 3)
- Search → Tavily API
- Currency → ExchangeRate API

---

## 🧪 Common Issues

### ❌ Rate Limit Error

```text
RateLimitError: GroqException
```

👉 Wait few seconds or upgrade plan

### ❌ YAML Key Error

```text
KeyError: 'intent_task'
```

👉 Ensure keys match `crew.py`

### ❌ Encoding Error

```text
UnicodeDecodeError
```

👉 Use:

```python
open(file, encoding="utf-8")
```

---

## 🚀 Future Improvements

- 📍 Google Maps integration
- 🖼️ Place images
- 📄 Export PDF itinerary
- 🌐 Deployment

---

## 👨‍💻 Author

Kaustav Roy Chowdhury

---

## ⭐ Support

If you like this project:
- ⭐ Star it
- 🍴 Fork it
- 📢 Share it

---

## 📜 License

MIT License

---

If you want next 🔥:

👉 Resume bullet points  
👉 LinkedIn post  
👉 GitHub description  

Just tell me 😄
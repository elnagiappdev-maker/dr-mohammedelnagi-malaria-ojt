
# 🚀 Deployment Guide — Malaria OJT App

This document explains how to deploy the bilingual malaria training app.

---

## ✅ Local Deployment
### Prerequisites
- Python 3.9+
- pip

### Steps
```bash
git clone https://github.com/<yourusername>/dr-mohammedelnagi-malaria-ojt.git
cd dr-mohammedelnagi-malaria-ojt
pip install -r requirements.txt
streamlit run app.py
```
Access on [http://localhost:8501](http://localhost:8501)

---

## ☁️ Streamlit Cloud Deployment
1. Sign in to [Streamlit Cloud](https://streamlit.io/cloud).
2. Create a **new app** from your GitHub repo.
3. Configure:
   - **Main file path:** `app.py`
   - **Branch:** `main`
4. Click **Deploy**.

The app will build automatically using `requirements.txt`.

---

## 🐳 Docker Deployment (optional)
```bash
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t malaria-ojt .
docker run -p 8501:8501 malaria-ojt
```

Access on [http://localhost:8501](http://localhost:8501)

---

## 🔐 Copyright Notice
All Rights Reserved © **Dr. Mohammedelnagi Mohammed (2025)**

Unauthorized use, modification, or distribution without written consent is prohibited.

# 🚀 Apache Airflow ETL – S3 → PostgreSQL

A complete ETL (Extract–Transform–Load) pipeline built using **Apache Airflow**, where data is extracted from **AWS S3**, transformed using Python scripts, and loaded into **PostgreSQL**.  
The project runs locally using **Docker Compose** and supports environment-based configuration.

---

## ✨ Features

- 📥 Extract raw data from AWS S3  
- 🔄 Transform & clean CSV/JSON files  
- 🗃 Load processed records into PostgreSQL  
- ⏱ Automated scheduling with Apache Airflow DAG  
- 🐳 Containerized using Docker Compose  
- 🔐 Secure configuration through environment variables  

---

## 📁 Project Structure

Apachi-Airflow-Flow-ETL/
│
├── dags/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── docker-compose.yaml
├── requirements.txt
├── README.md
└── .env (not included in git)

yaml
Copy code

---

## ⚙️ Environment Variables

Create a `.env` file in the project root and add:

Airflow User
AIRFLOW_WWW_USER_USERNAME=
AIRFLOW_WWW_USER_PASSWORD=

PostgreSQL Database
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
DB_PORT=

AWS S3 Credentials
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=

Airflow Security
AIRFLOW__WEBSERVER__SECRET_KEY=

yaml
Copy code

> ⚠️ **Important:** Never upload `.env` to GitHub.  

---

## 🐳 Running the Project with Docker

Ensure **Docker** and **Docker Compose** are installed.

### 1️⃣ Build Airflow Environment
```bash
docker compose build
2️⃣ Initialize Airflow Database
bash
Copy code
docker compose up airflow-init
3️⃣ Start all Airflow Services
bash
Copy code
docker compose up -d
4️⃣ Access Airflow UI
Visit:
👉 http://localhost:8080

Login using your .env Airflow credentials.

📌 ETL Pipeline Flow
scss
Copy code
Extract (S3) → Transform (Clean/Validate) → Load (PostgreSQL)
1. extract.py
Downloads required files from AWS S3

Saves them into a temporary folder

2. transform.py
Cleans, validates, and restructures the data

Performs conversions, handling nulls, formatting

3. load.py
Inserts transformed data into PostgreSQL

Creates table automatically if missing

🧪 Testing the ETL Pipeline
Open Airflow UI

Search for the ETL DAG

Enable the DAG

Click Trigger DAG

Track logs and execution from the Airflow UI.

📦 Technology Stack
Apache Airflow

Docker + Docker Compose

AWS S3

PostgreSQL

Python

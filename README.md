# Apache Airflow ETL Pipeline (S3 to PostgreSQL)

This project implements a complete ETL (Extract–Transform–Load) pipeline using Apache Airflow.  
The workflow extracts raw data from Amazon S3, transforms it using Python, and loads the processed output into PostgreSQL.  
The entire setup runs locally using Docker Compose for easy development and testing.

---

## Project Structure

```
Apachi-Airflow-Flow-ETL/
│
├── dags/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
# Airflow User
AIRFLOW_WWW_USER_USERNAME=
AIRFLOW_WWW_USER_PASSWORD=

# PostgreSQL
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=

# AWS S3
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=

# Airflow Security Key
AIRFLOW__WEBSERVER__SECRET_KEY=
```

---

## Running with Docker

Ensure Docker and Docker Compose are installed.

### 1. Build Airflow environment

```bash
docker compose build
```

### 2. Initialize Airflow

```bash
docker compose up airflow-init
```

### 3. Start services

```bash
docker compose up -d
```

### 4. Access Airflow UI

Navigate to: `http://localhost:8080`

Login using credentials defined in the `.env` file.

---

## ETL Workflow

### Extract
- Connects to S3
- Downloads raw files (CSV/JSON)

### Transform
- Cleans and preprocesses data
- Handles formatting and validation

### Load
- Loads data into PostgreSQL
- Creates table if required

---

## Triggering the Pipeline

1. Open Airflow UI
2. Locate the ETL DAG
3. Enable it
4. Trigger manually or let it run on schedule

Task-level logs and status can be monitored in the Airflow UI.

---

## Technologies Used

- **Apache Airflow**
- **Docker & Docker Compose**
- **AWS S3**
- **PostgreSQL**
- **Python**

---

## License

This project is open source .

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

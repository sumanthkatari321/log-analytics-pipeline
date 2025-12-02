# log-analytics-pipeline
End-to-end data engineering project that ingests web server logs, parses them, and prepares analytics-ready datasets for monitoring traffic, errors, and performance

# Log Analytics Data Engineering Pipeline

This project is the starting point of an end-to-end data engineering pipeline
built around web server log analytics. It includes simulated access logs that
represent realistic Nginx/Apache-style logs. Future versions of this project
will parse these logs, clean them, transform them into analytics datasets, and
load them into a database for monitoring traffic, latency, and error patterns.

---

## 📌 Current Features (v1)
- Generates realistic dummy web server access logs.
- Stores raw log files inside `data/raw_logs/`.
- Provides a foundation for adding parsing, aggregation, and ETL steps.

---

## 📁 Project Structure


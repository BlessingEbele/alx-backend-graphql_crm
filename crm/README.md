# CRM Project - Celery Report Setup

This guide explains how to set up and run Celery with Celery Beat to generate weekly CRM reports.

---

## 1. Install Redis and Dependencies

* Install Redis on Ubuntu/Debian:

```bash
sudo apt update
sudo apt install redis-server
```

* Start Redis:

```bash
sudo service redis-server start
```

* Verify Redis is running:

```bash
redis-cli ping
```

It should return:

```
PONG
```

* Install required Python dependencies:

```bash
pip install -r requirements.txt
```

---

## 2. Run Migrations

Apply database migrations:

```bash
python manage.py migrate
```

---

## 3. Start Celery Worker

Run the Celery worker in one terminal:

```bash
celery -A crm worker -l info
```

---

## 4. Start Celery Beat

Run Celery Beat in another terminal:

```bash
celery -A crm beat -l info
```

---

## 5. Verify Logs

Celery Beat will trigger scheduled tasks, and logs will be written to:

```
/tmp/crm_report_log.txt
```

Check logs with:

```bash
cat /tmp/crm_report_log.txt
```

Expected sample log:

```
2025-08-27 06:00:00 - Report: X customers, Y orders, Z revenue
```

---

## ⚡ Quick Commands (for local testing)

```bash
# Install Redis
sudo apt update && sudo apt install redis-server -y
sudo service redis-server start

# Verify Redis
redis-cli ping

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start Celery worker (Terminal 1)
celery -A crm worker -l info

# Start Celery Beat (Terminal 2)
celery -A crm beat -l info

# Verify logs
cat /tmp/crm_report_log.txt
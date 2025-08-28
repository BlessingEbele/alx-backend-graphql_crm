# CRM Project - Celery Setup with Celery Beat

This project uses **Celery** and **Celery Beat** to generate a **weekly CRM report** that summarizes:

* Total number of customers
* Total number of orders
* Total revenue

The report is logged to `/tmp/crm_report_log.txt` every **Monday at 06:00 AM**.

---

## 🚀 Setup Instructions

### 1. Install Dependencies

Ensure you have **Redis**, Celery, and Django Celery Beat installed.

```bash
# Install Redis (Ubuntu/Debian example)
sudo apt update
sudo apt install redis-server -y

# Start Redis
sudo service redis-server start

# Install Python dependencies
pip install -r requirements.txt
```

Make sure `requirements.txt` includes:

```
celery
django-celery-beat
redis
gql
```

---

### 2. Update Django Settings

In **`crm/settings.py`**, ensure the following:

```python
INSTALLED_APPS = [
    # Django default apps...
    'django_celery_beat',
]

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_BEAT_SCHEDULE = {
    'generate-crm-report': {
        'task': 'crm.tasks.generate_crm_report',
        'schedule': crontab(day_of_week='mon', hour=6, minute=0),
    },
}
```

---

### 3. Initialize Celery

* In **`crm/celery.py`**, configure Celery.
* In **`crm/__init__.py`**, ensure Celery loads automatically.

---

### 4. Run Database Migrations

```bash
python manage.py migrate
```

---

### 5. Start Celery Worker

Run the Celery worker to process tasks:

```bash
celery -A crm worker -l info
```

---

### 6. Start Celery Beat

Run Celery Beat to schedule the weekly report:

```bash
celery -A crm beat -l info
```

---

### 7. Verify Logs

The report will be written to:

```bash
cat /tmp/crm_report_log.txt
```

You should see output similar to:

```
2025-08-27 06:00:00 - Report: 50 customers, 200 orders, 1,000,000 revenue
```
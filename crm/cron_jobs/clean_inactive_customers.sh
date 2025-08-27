#!/bin/bash
# Script to clean inactive customers (no orders in the last year)

# Run Django shell command
deleted_count=$(python3 /path/to/your/project/manage.py shell -c "
from django.utils import timezone
from datetime import timedelta
from crm.models import Customer

cutoff_date = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(
    orders__isnull=True,
    created_at__lt=cutoff_date
)

count = inactive_customers.count()
inactive_customers.delete()
print(count)
")

# Log output with timestamp
echo \"\$(date '+%Y-%m-%d %H:%M:%S') - Deleted \$deleted_count inactive customers\" >> /tmp/customer_cleanup_log.txt

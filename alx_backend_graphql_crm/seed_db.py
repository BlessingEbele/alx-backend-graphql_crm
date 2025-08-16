import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_backend_graphql_crm.settings")
django.setup()

from crm.models import Customer, Product

# Sample seed data
Customer.objects.create(name="John Doe", email="john@example.com", phone="+1234567890")
Product.objects.create(name="Phone", price=299.99, stock=50)
Product.objects.create(name="Tablet", price=499.99, stock=30)

print("Database seeded successfully!")

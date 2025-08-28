#!/usr/bin/env python3
import sys
import logging
from datetime import datetime, timedelta
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Configure logging
logging.basicConfig(
    filename="/tmp/order_reminders_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def main():
    try:
        # GraphQL transport
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=True,
            retries=3,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Query for orders within the last 7 days
        last_week = (datetime.now() - timedelta(days=7)).date().isoformat()
        query = gql(
            """
            query GetRecentOrders($lastWeek: Date!) {
                orders(orderDate_Gte: $lastWeek) {
                    id
                    customer {
                        email
                    }
                }
            }
            """
        )

        variables = {"lastWeek": last_week}
        result = client.execute(query, variable_values=variables)

        # Log each order reminder
        for order in result.get("orders", []):
            order_id = order["id"]
            customer_email = order["customer"]["email"]
            logging.info(f"Reminder: Order ID {order_id} for {customer_email}")

        print("Order reminders processed!")

    except Exception as e:
        logging.error(f"Error processing order reminders: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

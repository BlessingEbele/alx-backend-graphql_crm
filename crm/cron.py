import datetime
import os

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    # Format current time
    now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

    # Log message
    message = f"{now} CRM is alive\n"

    # Append to log file
    log_file = "/tmp/crm_heartbeat_log.txt"
    with open(log_file, "a") as f:
        f.write(message)

    # Optional: verify GraphQL hello endpoint
    try:
        transport = RequestsHTTPTransport(
            url="http://127.0.0.1:8000/graphql/",
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql("{ hello }")
        response = client.execute(query)
        with open(log_file, "a") as f:
            f.write(f"GraphQL hello: {response}\n")
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"GraphQL check failed: {e}\n")

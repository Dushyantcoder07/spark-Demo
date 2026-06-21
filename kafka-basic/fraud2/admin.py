from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "fraud-notification",
    bootstrap_servers=["kafka:9092"],
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    )
)

print("\n=== ADMIN FRAUD DASHBOARD ===\n")

count = 0

for message in consumer:

    data = message.value

    count += 1

    print("=" * 50)
    print(f"ALERT #{count}")
    print("=" * 50)

    print(f"User ID        : {data.get('userId')}")
    print(f"Name           : {data.get('name')}")
    print(f"Email          : {data.get('email')}")
    print(f"Amount         : ₹{data.get('amount')}")
    print(f"Status         : {data.get('account_status')}")
    print(f"Transaction ID : {data.get('tx_id')}")

    print("=" * 50)
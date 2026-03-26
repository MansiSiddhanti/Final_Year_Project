from datetime import datetime, timedelta

def generate_report():
    # Dummy data for now (since no IoT yet)
    today = datetime.today()

    data = []

    for i in range(10):
        day = (today - timedelta(days=i)).strftime("%Y-%m-%d")

        data.append({
            "date": day,
            "water_used": 100 + i * 10
        })

    return {
        "irrigation_events": data
    }
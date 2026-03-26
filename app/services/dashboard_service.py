def get_dashboard_data():
    """
    Returns summary data for dashboard view
    """
    return {
        "status": "success",
        "dashboard": {
            "active_crops": 5,
            "soil_moisture_avg": 42,
            "today_irrigation": "ON",
            "alerts": 1
        }
    }

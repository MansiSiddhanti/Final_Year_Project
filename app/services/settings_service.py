settings = {
    "auto_irrigation": True,
    "irrigation_threshold": 30,
    "notifications": True
}

def get_settings():
    return settings

def update_settings(new_settings: dict):
    settings.update(new_settings)
    return settings

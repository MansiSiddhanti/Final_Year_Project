# irrigation_control.py

motor_status = "OFF"

def turn_motor_on():
    global motor_status
    motor_status = "ON"
    print("💧 Irrigation motor turned ON")
    return motor_status


def turn_motor_off():
    global motor_status
    motor_status = "OFF"
    print("🚫 Irrigation motor turned OFF")
    return motor_status


def get_motor_status():
    return motor_status

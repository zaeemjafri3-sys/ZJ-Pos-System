import serial

for port in ["COM3", "COM4", "COM5", "COM6"]:
    try:
        s = serial.Serial(port, 9600, timeout=1)
        print("WORKING:", port)
        s.close()
    except Exception as e:
        print("FAILED:", port)
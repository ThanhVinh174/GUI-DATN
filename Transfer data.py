import serial

ser = 0

def init_serial():
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM1'
    ser.timeout = 10
    ser.open()

init_serial()

while True:
    data = []
    data.append(ser.read())
    print(data)

ser.close()


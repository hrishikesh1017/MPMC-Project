import serial

# Define the serial port and baud rate (must match Arduino settings)
serial_port = 'COM5'  # Replace with your Arduino's serial port
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)
if not ser.isOpen():
    ser.open()
print('com5 is open', ser.isOpen())

# Create and open a text file for writing
with open('data.txt', 'w') as file:
    while True:
        # Read data from the serial port
        line = ser.readline().decode('utf-8').strip()
        print(line)  # Optional: Print the data to the console
        file.write(line + '\n')

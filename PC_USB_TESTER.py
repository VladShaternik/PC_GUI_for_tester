import serial

print('Connecting to COM7')
s = serial.Serial('COM7')

print('Writing 5')
s.write(b'\x05')

res = b'\x00'

print('Reading values')
while res == b'\x00':
    res = s.read()
    print("-- ", res)

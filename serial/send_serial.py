import serial
import time
from struct import *

COM = '/dev/ttyAMA0'

ser = serial.Serial(COM, 115200)   

# 変数は適宜変更して下さい．
X=109.243
Y=-209
Z=3098

while True:

    data = pack('>ddd', X, Y, Z) # エンコードする変数の数にあわせて，'d'の数も増やして下さい．
    data = data + b'\n'
    ser.write(data)

    time.sleep(1)
    
ser.close()     
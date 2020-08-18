import serial
import time
import simplestm32_pb2
ser = serial.Serial('COM4', 115200, timeout=0,parity=serial.PARITY_NONE, rtscts=1)


tmsg=simplestm32_pb2.comMessage()


while True:
    time.sleep(0.2)
    buff=ser.readline().strip()        
    if len(buff)!=0:
        tmsg.ParseFromString(buff)
        print(tmsg.pot_val1,tmsg.pot_val2)
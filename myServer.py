import socket
import network
import time
import machine

wifi=network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect('WiFi Name','password')

while wifi.isconnected()==False:
    print("waiting for connection...")
    time.sleep(1)
wifiInfo=wifi.ifconfig()
print(wifiInfo)
ServerIP=wifiInfo[0]
ServerPort=2222
bufferSize=1024
UDPServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPServer.bind((ServerIP,ServerPort))
print("UDP Server up and Waiting")
led = machine.Pin(15, machine.Pin.OUT)

# Main loop to receive messages and control LED
while True:
    message, address = UDPServer.recvfrom(bufferSize)
    messageDecoded = message.decode('utf-8').strip()
    print(f"Received message from {address}: {messageDecoded}")
    
    # Control the LED based on the received message
    if messageDecoded == 'Y':
        led.value(1)
        print("LED turned ON")
    else:
        led.value(0)
        print("LED turned OFF")




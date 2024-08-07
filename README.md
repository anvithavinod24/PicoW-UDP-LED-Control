This project demonstrates how to control an LED connected to a Raspberry Pi Pico W using UDP commands over a WiFi network.
It uses the UDP (User Datagram Protocol)

The client is in the local machine. It continuously takes user input data. In this case, it takes 'Y' as LED ON and any other variable as LED OFF. 
This message is then encoded and sent as UDP Message to the server's address and port. The client also prints a confirmation message everytime it sends a command. 

The RPI Pico W is connected to the WiFi and listens to IP Address and port 2222 for any incoming messages. When it recieves any message, it decodes it and then prints it.
In this case, when 'Y' is recieved from the client, the LED is turned on. 

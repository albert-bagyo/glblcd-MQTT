import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")
        
Connected = False  # global variable for the state of the connection

client = mqtt.Client()
client.on_connect = on_connect
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)
    
try:
    while True:
        topic = input("Blink Who: ")
        blink_count = int(input("How many times: "))
        for i in range(blink_count):
            client.publish(f"glblcd/{topic}", 'on')
            time.sleep(1)
            client.publish(f"glblcd/{topic}", 'off')
        

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()

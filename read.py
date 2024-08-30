import paho.mqtt.client as mqtt
from gpiozero import LED

led = LED(17)
buzz = LED(27)
led_on = False
buzz_on = False

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe("glblcd/lightbulb")
    client.subscribe("glblcd/bagyo")
    #client.subscribe("BUZZER")
    
def on_message(client, userdata, msg):
    global led, led_on,buzz, buzz_on
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")
    m = msg.payload.decode("utf-8")
    if m == 'on':
        led.on()
    elif m == 'off':
        led.off()
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
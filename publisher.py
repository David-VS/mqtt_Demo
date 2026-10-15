from paho.mqtt import client
import time

broker = 'i16179da.ala.eu-central-1.emqxsl.com'
port = 8883
username='JohnEhb'
password='test1234'


def connect_mqtt():
    def on_connect(client, userdata, connect_flags, reason_code, properties):
        if reason_code == 0:
            print('verbonden!')
        else:
            print(f'verbindingsprobleem {reason_code}')

    myClient = client.Client(client.CallbackAPIVersion.VERSION2, "myPublisher")
    myClient.tls_set(ca_certs='./certs/emqxsl-ca.crt')
    myClient.username_pw_set(username, password)
    myClient.on_connect = on_connect
    myClient.connect(broker, port)
    
    return myClient

def on_publish(client, userdata, mid, reason_code, properties):
    if reason_code == 0:
        print('message verzonden')
    else:
        print(f'probleem {reason_code} om te verzenden')


def run():
    myClient = connect_mqtt()

    myClient.on_publish = on_publish
    myClient.loop_start()

    while True:
        message = input('wat is je bericht?')
        myClient.publish("demo/message", message, qos=1)
        time.sleep(5)
    

run()
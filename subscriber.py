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

    myClient = client.Client(client.CallbackAPIVersion.VERSION2, "mySubscriber")
    myClient.tls_set(ca_certs='./certs/emqxsl-ca.crt')
    myClient.username_pw_set(username, password)
    myClient.on_connect = on_connect
    myClient.connect(broker, port)
    
    return myClient

def on_message(client, userdata, message):
    print(message.topic, message.payload)


def run():
    myClient = connect_mqtt()
    myClient.on_message = on_message
    myClient.loop_start()
    myClient.subscribe("demo/message", qos=1)
    while True:
        time.sleep(5)

run()
# producer.py
# This script will publish MQ message to my_exchange MQ exchange
import pika
import keyboard

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.99', 5672, '/Jcaldwell', pika.PlainCredentials('Jcaldwell', 'Jcaldwell')))
channel = connection.channel()

while True:
    key_press = keyboard.read_key()
    send_var = "STP"
    if key_press == "w":
        send_var = "FWD"

    if key_press == "a":
        send_var = "SLT"

    if key_press == "s":
        send_var = "BAK"

    if key_press == "d":
        send_var = "SRT"

    if key_press == "q":
        send_var = "FLT"

    if key_press == "e":
        send_var = "FRT"

    if key_press == "z":
        send_var = "BLT"

    if key_press == "c":
        send_var = "BRT"
    channel.basic_publish(exchange='Exchange_Jcaldwell', routing_key='1111', body=send_var)

connection.close()

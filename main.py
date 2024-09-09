#  Name: mohammad Khdour - ID:1212517
#  Name: mohammad Ataya - ID: 1211555
#  Name: Hamza Alqam - ID:1211173

from socket import *
import threading
import time

def sending(client,first_name, last_name):
    while True:
        message = input("Enter your message: ")
        sendingTime = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
        full_message = f"{first_name}|{last_name}|{message}|{sendingTime}"
        if message[:-1].isdigit() and message.endswith("D"):
            number = int(message[:-1])
            try:
                print(messages[number - 1])
            except:
                print('out of range')
        else:
            client.sendto(full_message.encode(), ('26.255.255.255', port))

def listening(server):

    while True:
            data, address = server.recvfrom(2048)
            message = data.decode()
            #print(address[0])
            if address[0] != host:
                displayMessage(message)


def displayMessage(message):
    firstname, lastname, Message, Ricevetime = message.split('|')
    messages.append(Message)
    print(f"\n Received: {Message}  from {firstname} {lastname} at {Ricevetime}")

def main():
    global host, port, clients, messages, broadcast_ip
    messages = []
    clients = []
    host = '26.183.197.207'
    port = 5051
    print(host)
    client = socket(AF_INET, SOCK_DGRAM)
    #client.bind((host, port))
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(('', port))

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    t1 = threading.Thread(target=sending ,args=(client, first_name, last_name,))
    t2 = threading.Thread(target=listening, args=(server,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

main()
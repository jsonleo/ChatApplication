import socket
import sys
import time

s = socket.socket()
port = 50000
s.connect(('192.168.0.7',port))
print(" Berhasil dihubungkan ke server ")
while 1:
            incoming_message = s.recv(1024)
            incoming_message = incoming_message.decode()
            if (incoming_message=="attach"):
                print(" Server : ", incoming_message)
                print("")
                filename =  input(str("Masukkan nama file yang ingin diterima: "))
                file = open(filename,'wb' )
                file_data = s.recv(9000000)
                file.write(file_data)
                file.close()
                print("File telah sukses diterima ")
            else:
                print(" Server : ", incoming_message)
                print("")
                message = input(str(">> "))
                if (message=="attach"):
                    message = message.encode()
                    s.send(message)
                    print(" Pesan Telah Terkirim ")
                    print("")
                    filename = input(str(" Masukkan nama file yang ingin dikirim: "))
                    file = open(filename, 'rb')
                    file_data = file.read(9000000) 
                    s.send(file_data)
                    print(" File telah terkirim ")
                else :
                    message = message.encode()
                    s.send(message)
                    print(" Pesan telah terkirim ")
                    print("")

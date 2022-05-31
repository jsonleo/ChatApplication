import socket
import sys
import time

s = socket.socket()
print(" Server akan mulai pada ip adress: ", '192.168.0.6')
port = 50000
s.bind(('192.168.0.6',port))
print("")
print(" Server sukses terhubung ke ip adress dan port ")
print("")
print(" Server menunggu koneksi lainnya ")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, " Sudah terhubung ke server dan sekarang online.. ")
print("")
while 1:
            message = input(str(">> "))
            if (message=="attach"):
                message = message.encode()
                conn.send(message)
                print(" Pesan Telah Terkirim ")
                print("")
                filename = input(str(" Masukkan nama file yang ingin dikirim: "))
                file = open(filename, 'rb')
                file_data = file.read(9000000) 
                conn.send(file_data)
                print(" File telah terkirim ")
            else :
                message = message.encode()
                conn.send(message)
                print(" Pesan Telah Terkirim ")
                print("")
                incoming_message = conn.recv(1024)
                incoming_message = incoming_message.decode()
                if (incoming_message=="attach"):
                    print(" Server : ", incoming_message)
                    print("")
                    filename =  input(str("Masukkan nama file yang ingin diterima: "))
                    file = open(filename,'wb' )
                    file_data = conn.recv(9000000)
                    file.write(file_data)
                    file.close()
                    print("File telah sukses diterima ")
                else:
                    print(" Client : ", incoming_message)
                    print("")

            

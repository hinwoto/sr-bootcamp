import getpass
import sys
import telnetlib

HOST = "198.18.1.41"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("router isis 1\n")
tn.write("address-family ipv4 unicast\n")
tn.write("segment-routing prefix-sid-map advertise-local\n")
tn.write("exit\n")
tn.write("exit\n")
tn.write("segment-routing\n")
tn.write("mapping-server\n")
tn.write("prefix-sid-map\n")
tn.write("address-family ipv4\n")
tn.write("1.1.1.2/32 2 range 3\n")

tn.write("commit\n")
tn.write("end\n")
tn.write("show run segment-routing\n")
tn.write("exit\n")

print tn.read_all()

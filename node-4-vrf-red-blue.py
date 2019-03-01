import getpass
import sys
import telnetlib

HOST = "198.18.1.44"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("vrf red\n")
tn.write("address-family ipv4 uni\n")
tn.write("import route-target 45:45\n")
tn.write("export route-target 45:45\n")
tn.write("vrf blue\n")
tn.write("address-family ipv4 uni\n")
tn.write("import route-target 450:450\n")
tn.write("export route-target 450:450\n")
tn.write("exit\n")
tn.write("exit\n")
tn.write("int lo4\n")
tn.write("vrf red\n")
tn.write("ipv4 address 4.4.4.4 255.255.255.255\n")
tn.write("no shut\n")
tn.write("int lo14\n")
tn.write("vrf blue\n")
tn.write("ipv4 address 14.14.14.14 255.255.255.255\n")
tn.write("no shut\n")
tn.write("int lo40\n")
tn.write("vrf red\n")
tn.write("ipv4 address 40.40.40.40 255.255.255.255\n")
tn.write("no shut\n")
tn.write("int lo44\n")
tn.write("vrf red\n")
tn.write("no ip address\n")
tn.write("ipv4 address 44.44.44.44 255.255.255.255\n")
tn.write("no shut\n")
tn.write("int lo144\n")
tn.write("vrf blue\n")
tn.write("ipv4 address 144.144.144.144 255.255.255.255\n")
tn.write("no shut\n")
tn.write("int lo140\n")
tn.write("vrf blue\n")
tn.write("ipv4 address 140.140.140.140 255.255.255.255\n")
tn.write("no shut\n")
tn.write("exit\n")
tn.write("router bgp 65000\n")
tn.write("neighbor-group RR-services-group\n")
tn.write("address-family vpnv4 unicast\n")
tn.write("route-policy SET_COLOR_IN in\n")
tn.write("vrf red\n")
tn.write("rd 45:45\n")
tn.write("address-family ipv4 unicast\n")
tn.write("redis connected\n")
tn.write("vrf blue\n")
tn.write("rd 450:450\n")
tn.write("address-family ipv4 unicast\n")
tn.write("redis connected\n")
tn.write("extcommunity-set opaque 5\n")
tn.write("5 end-set\n")
tn.write("extcommunity-set opaque 15\n")
tn.write("15 end-set\n")
tn.write("extcommunity-set opaque 50\n")
tn.write("50 end-set\n")
tn.write("extcommunity-set opaque 55\n")
tn.write("55 end-set\n")
tn.write("extcommunity-set opaque 150\n")
tn.write("150 end-set\n")
tn.write("extcommunity-set opaque 155\n")
tn.write("155 end-set\n")
tn.write("route-policy SET_COLOR_IN\n")
tn.write("if rd in (45:45) and destination in (5.5.5.5/32) then\n")
tn.write("set extcommunity color 5\n")
tn.write("elseif rd in (45:45) and destination in (50.50.50.50/32) then\n")
tn.write("set extcommunity color 5\n")
tn.write("elseif rd in (45:45) then\n")
tn.write("set extcommunity color 5\n")
tn.write("elseif rd in (450:450) and destination in (15.15.15.15/32) then\n")
tn.write("set extcommunity color 15\n")
tn.write("elseif rd in (450:450) and destination in (150.150.150.150/32) then\n")
tn.write("set extcommunity color 150\n")
tn.write("elseif rd in (450:450) then\n")
tn.write("set extcommunity color 155\n")
tn.write("else pass endif\n")
tn.write("end-policy\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show vrf all\n")
tn.write("exit\n")

print tn.read_all()
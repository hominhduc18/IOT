from urllib import request, parse   # khai báo thư viện urllib
from time import sleep  # khai báo thư viện time 
from seeed_dht import DHT   # khai báo thư viện cảm biến dht
from grove.display.jhd1802 import JHD1802   
from random import randint                       
sensor = DHT('11',5)     # cảm biến DHT11 kết nối chân D5
def make_param_thingspeak(temp, humi, data):   # khai báo biến param
	params = parse.urlencode({'field1': temp,'field2': humi,'field3': data}).encode()	#gán giá trị vào field
	return params
def thingspeak_post(params): 
	api_key_write = "RTP192G9W94TJTIT"   #chèn api_key 
	req = request.Request('https://api.thingspeak.com/update',method = "POST")  
	req.add_header("Content-Type", "application/x-www-form-urlencoded")
	req.add_header("X-THINGSPEAKAPIKEY", api_key_write)
	r = request.urlopen(req, data = params)
	reponse_data = r.read()
	return reponse_data
while True:
        data_random = randint(0,100)  # random giá trị 0 đến 100
        print('Random {}'.format(data_random))#in gia tri random
        humi, temp = sensor.read()   # trả giá trị nhiệt độ, độ ẩm từ cảm biến
        print('Nhiet do: {}*C\nDo am: {}%'.format(temp,humi))  # xuất gia trị 
        params_thingspeak = make_param_thingspeak(humi, temp, data_random)  
        thingspeak_post(params_thingspeak)
        sleep(20)  # sau 20giay tín hiệu gửi lên sever
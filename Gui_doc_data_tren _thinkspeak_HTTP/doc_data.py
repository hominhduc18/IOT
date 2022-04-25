from grove.display.jhd1802 import JHD1802 
from gpiozero import LED   
from grove.grove_relay import GroveRelay  
from time import sleep  
from urllib import request, parse
import json
lcd = JHD1802()
led = LED(5)      
relay = GroveRelay(16)  
buzzer = LED(18)  
def thingspeak_get():
    api_key_read = "4P1TXP3Q4ACHQPUS"    
    channel_ID = "1712204"   
    req = request.Request("https://api.thingspeak.com/channels/%s/fields/1/last.json?api_key=%s" %(channel_ID,api_key_read), method="GET")
    r = request.urlopen(req)  
    respone_data = r.read().decode()   
    respone_data = json.loads(respone_data)
    value = respone_data["field1"]     
    return value
def thingspeak_get1():
    api_key_read = "4P1TXP3Q4ACHQPUS"  
    channel_ID = "1712204"     
    req1 = request.Request("https://api.thingspeak.com/channels/%s/fields/2/last.json?api_key=%s" %(channel_ID,api_key_read), method="GET") 
    r1 = request.urlopen(req1)
    respone_data = r1.read().decode()
    respone_data = json.loads(respone_data)
    value = respone_data["field2"]
    return value
def thingspeak_get2():
    api_key_read = "4P1TXP3Q4ACHQPUS"      
    channel_ID = "1712204"   
    req2 = request.Request("https://api.thingspeak.com/channels/%s/fields/3/last.json?api_key=%s" %(channel_ID,api_key_read), method="GET")     
    r2 = request.urlopen(req2 )
    respone_data = r2.read().decode()
    respone_data = json.loads(respone_data)
    value = respone_data["field3"]
    return value
while True:
    humi = thingspeak_get()
    print('Do am : {}%'.format(humi)) 
    temp = thingspeak_get1()
    print('Nhiet do : {}*C'.format(temp))  
    rd = thingspeak_get2()
    print('Random: {}\n'.format(rd))  
    lcd.setCursor(0, 0)
    lcd.write('DA:{}%' .format(humi))  
    lcd.setCursor(0, 9)
    lcd.write('ND:{}*C' .format(temp))   
    lcd.setCursor(1, 0)
    lcd.write('RANDOM:{0:2}' .format(rd))  
    if int(rd) > 50:    
        led.on()
    elif int(rd) <= 50:  
        led.off()
    if int(humi) > 70:   
        relay.on()
    elif int(humi) < 65:   
        relay.off()
    if int(temp) >30:   
        buzzer.on()
    elif int(temp) <25:
        buzzer.off()
        
    sleep(20)
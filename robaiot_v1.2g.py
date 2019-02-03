import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
import urllib.request as urllib2
import json
#ECHO = 27

IO.setup(2,IO.IN) #GPIO 2 -> Left IR out
IO.setup(3,IO.IN) #GPIO 3 -> Right IR out
#IO.setup(ECHO,IO.IN)

IO.setup(22,IO.OUT)
IO.setup(25,IO.OUT)
IO.setup(4,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(14,IO.OUT) #GPIO 14 -> Motor 1 terminal B

IO.setup(17,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(18,IO.OUT) #GPIO 18 -> Motor Left terminal B

pwm1=IO.PWM(22,100)
pwm2=IO.PWM(25,100)
pwm1.start(0)
pwm2.start(0)

READ_API_KEY='######' #thingspeak api key -> string
CHANNEL_ID= 1234567890     #thingspeak Channel ID -> numeric

def main():
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    print("http status code=%s" % (conn.getcode()))
    data=json.loads(response.decode('utf-8'))
    
   # print(data['field1'],data['created_at'])
    conn.close()
    return data

data=main()
print(data['field5'])
#print(type(data['field5']))
#a='1'
#b=2
#print(type(a))
#print(type(b))
while 1:
    #if __name__ == '__main__':
    

 

    if(IO.input(2)==False and IO.input(3)==False): #both while move forward
        IO.output(22,IO.LOW)
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-
        pwm1.ChangeDutyCycle(25)
        IO.output(22,IO.HIGH)
        

        IO.output(25,IO.LOW)
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-
        pwm2.ChangeDutyCycle(25)
        IO.output(25,IO.HIGH)
        
        
        

    elif(IO.input(2)==False and IO.input(3)==True): #turn right
        IO.output(22,IO.LOW)
        IO.output(4,False) #1A+
        IO.output(14,True) #1B-
        pwm1.ChangeDutyCycle(100)
        IO.output(22,IO.HIGH)
        
        #pwm1.ChangeDutyCycle(1)
        #IO.output(22,True)

        IO.output(25,IO.LOW)
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-
        pwm2.ChangeDutyCycle(100)
        IO.output(25,IO.HIGH)
        
        #pwm2.ChangeDutyCycle(1)
        #IO.output(25,True)

    elif(IO.input(2)==True and IO.input(3)==False): #turn left
        IO.output(22,IO.LOW)
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-
        pwm1.ChangeDutyCycle(100)
        IO.output(22,IO.HIGH)
        
        #pwm1.ChangeDutyCycle(1)
        #IO.output(22,True)
        IO.output(25,IO.LOW)

        IO.output(17,False) #2A+
        IO.output(18,True) #2B-
        pwm2.ChangeDutyCycle(100)
        IO.output(25,IO.HIGH)
        
        #pwm2.ChangeDutyCycle(1)
        #IO.output(25,True)
    
    elif(IO.input(2)==True and IO.input(3)==True and data['field5']=='1'): #take decision RIGHT
        
        IO.output(22,IO.LOW)
        IO.output(4,False) #1A+
        IO.output(14,True) #1B-
        pwm1.ChangeDutyCycle(25)
        IO.output(22,IO.HIGH)
        

        IO.output(25,IO.LOW)
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-
        pwm2.ChangeDutyCycle(25)
        IO.output(25,IO.HIGH)
        
    elif(IO.input(2)==True and IO.input(3)==True and data['field5']=='2'): #take decision LEFT
        IO.output(22,IO.LOW)
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-
        pwm1.ChangeDutyCycle(25)
        IO.output(22,IO.HIGH)
        
        IO.output(25,IO.LOW)
        IO.output(17,False) #2A+
        IO.output(18,True) #2B-
        pwm2.ChangeDutyCycle(25)
        IO.output(25,IO.HIGH)

    else:  #stay still
        IO.output(22,IO.LOW)
        
        IO.output(4,True) #1A+
        IO.output(14,True) #1B-
        pwm1.ChangeDutyCycle(40)
        IO.output(22,IO.HIGH)
        
        #pwm1.ChangeDutyCycle(1)
        #IO.output(22,True)
        IO.output(25,IO.LOW)

        IO.output(17,True) #2A+
        IO.output(18,True) #2B-
        pwm2.ChangeDutyCycle(40)
        IO.output(25,IO.HIGH)
        
        #pwm2.ChangeDutyCycle(1)
        #IO.output(25,True)

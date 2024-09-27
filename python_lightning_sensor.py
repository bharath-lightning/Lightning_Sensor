#Importing libraries
import serial 
import time 
import streamlit as st 


arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1) 
def write_read(x): 
     arduino.write(bytes(x, 'utf-8')) 
     # time.sleep(0.05) 
     time.sleep(1)
     data = arduino.readline() 
     return data 
     
while True: 
     # num = input("Enter a number: ")  Taking input from user 
     num = str(0)
     value = write_read(num) 
     print(value) # printing the value
     st.text(value)                   
     

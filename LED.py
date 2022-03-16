#!/usr/bin/env python3
import RPi.GPIO as gpio
import time

# Configurando como BCM, Pinos Físicos
gpio.setmode(gpio.BCM)

# Configurando a direção do Pino
gpio.setup(5, gpio.OUT)
while True:
    gpio.output(5, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(5, gpio.LOW)
    time.sleep(0.1)
    
# Desfazendo as modificações do GPIO
gpio.cleanup()

    
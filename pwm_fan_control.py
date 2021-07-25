#!/usr/bin/python
import pigpio
import time

servo = 13

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo, 25000)
pwm.set_PWM_range(servo, 100)
while True:
    # get CPU temp
    with open("/sys/class/thermal/thermal_zone0/temp") as file:
        temp = float(file.read()) / 1000.00
        temp = float('%.2f' % temp)

    fun_speed = 0
    if 50 <= temp > 30:
        fun_speed = 40
    elif 55 <= temp > 50:
        fun_speed = 50
    elif 60 <= temp > 55:
        fun_speed = 75
    elif 65 <= temp > 60:
        fun_speed = 90
    elif temp > 65:
        fun_speed = 100
    pwm.set_PWM_dutycycle(servo, fun_speed)
    time.sleep(1)

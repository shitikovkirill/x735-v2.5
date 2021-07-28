import pigpio


class ReedFan:
    __slots__ = ['pin', 'pi']

    def __init__(self):
        self.pin = 16
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin, pigpio.INPUT)
        self.pi.set_pull_up_down(self.pin, pigpio.PUD_UP)

    def get_turnover(self):
        return self.pi.wait_for_event(self.pin, 5*60)


class SetFan:
    
    __slots__ = ['pin', 'pwm']

    def __init__(self):
        self.pin = 13
        self.pwm = pigpio.pi()
        self.pwm.set_mode(self.pin, pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(self.pin, 25000)
        self.pwm.set_PWM_range(self.pin, 100)
        
    def set_speed(self, speed):
        self.pwm.set_PWM_dutycycle(self.pin, speed)


def get_cpu_temp():
    """
    Get temperature from cpu
    """
    with open("/sys/class/thermal/thermal_zone0/temp") as file:
        temp = float(file.read()) / 1000.00
        temp = float('%.2f' % temp)
    return temp


def get_fun_speed(temp):
    """
    Calculate fun speed by temperature
    """
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
    return fun_speed


#!/usr/bin/python
import os
import subprocess as sub
import time
icmp_filter="ICMP echo request"
greenled_trigger = 'sudo sh -c "echo none > /sys/class/leds/green:ph07:led4/trigger"'
greenled_on = 'sudo sh -c "echo 1 > /sys/class/leds/green:ph07:led4/brightness"'
greenled_off = 'sudo sh -c "echo 0 > /sys/class/leds/green:ph07:led4/brightness"'
os.system(greenled_trigger)
loop_count = 0;
def display_led_off():
        #os.system(blueled_off)
        os.system(greenled_off)
        time.sleep(0.5)
def display_led_on():
        #os.system(blueled_on)
        os.system(greenled_on)
        time.sleep(0.5)

def blink():
        display_led_on()
        display_led_off()

def run_blink():
        global loop_count
        if loop_count == 0:
                loop_count = 1
                blink()
                print('start')
                loop_count = 0;

def check_icmp():
        global icmp_filter
        p = sub.Popen(('sudo', 'tcpdump', '-l'), stdout=sub.PIPE)
        while True:
                line = p.stdout.readline()
                if line.find(icmp_filter) != -1:
                        print(line)
                        run_blink()

def main():
        display_led_off()
        check_icmp()

if __name__ == "__main__":
        main()



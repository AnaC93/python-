from time import sleep

class TrafficLight:
    __color = "Black"

    def running(self):
        while True:
            print("Red")
            sleep(7)
            print("Yellow")
            sleep(2)
            print("Green")
            sleep(7)
            print("Yellow")
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()
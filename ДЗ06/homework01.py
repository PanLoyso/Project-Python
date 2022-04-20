from time import sleep
from datetime import datetime as dt

class TrafficLight:
    _states = {'red': 7, 'yellow': 2, 'green': 10}
    _color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"Горит {self._color} светофор"
                  f" {sw_time} секунды")

            sleep(sw_time)

            print(f"Переключение светофора с {self._color} после " 
                  f"{(dt.now() - start_state_time).seconds} секунд ожидания")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()

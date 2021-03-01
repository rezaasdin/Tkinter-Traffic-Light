class TrafficLight():

    def __init__(self):
        self.green_state = GreenState(self)
        self.yellow_state = YellowState(self)
        self.red_state = RedState(self)
        self.state = self.red_state
       

    def change_state(self):
        self.state.handle_request()

    def get_green_light_state(self):
        return self.green_state

    def get_yellow_light_state(self):
        return self.yellow_state

    def get_red_light_state(self):
        return self.red_state

    def set_state(self, state):
        self.state = state

    def __str__(self):
        return '{} {} {} {}'.format(self.green_state, self.yellow_state, self.red_state, self.state)


class State():

    def handle_request(self):
        pass

    def __str__(self):
        return 'red'


class RedState(State):

    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def handle_request(self):
        print('Wait for turning traffic light to green...')
        self.traffic_light.set_state(self.traffic_light.get_green_light_state())

    def __str__(self):
        return 'Traffic light is on red.'


class YellowState(State):

    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def handle_request(self):
        print('Wait for turning traffic light to red...')
        self.traffic_light.set_state(self.traffic_light.get_red_light_state())

    def __str__(self):
        return 'Traffic light is on yellow.'


class GreenState(State):

    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def handle_request(self):
        print('Wait for turning traffic light to yellow...')
        self.traffic_light.set_state(self.traffic_light.get_yellow_light_state())

    def __str__(self):
        return 'Traffic light is on green.'


tr = TrafficLight()
rd_s = RedState(tr)
yl_s = YellowState(tr)
gr_s = GreenState(tr)

import time

first = True

while True:
    
    if first:
        first = False
        print(tr.state)
        
    rd_s.handle_request()
    time.sleep(2)
    print(tr.state)
    gr_s.handle_request()
    time.sleep(2)
    print(tr.state)
    yl_s.handle_request()
    time.sleep(2)
    print(tr.state)

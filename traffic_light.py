from Tkinter import *
time_interval = 2000    # You can change this (Default = 2 Seconds)

window = Tk()

class TrafficLight():

    def __init__(self):
        self.green_state = GreenState(self)
        self.yellow_state = YellowState(self)
        self.red_state = RedState(self)
        self.state = self.red_state

        
        window.title("Traffic Light")

        frame = Frame(window)
        frame.pack()
        self.color = StringVar()
        self.canvas = Canvas(window, width=120, height=350, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(10, 120, 110, 220, fill="white")
        self.oval_green = self.canvas.create_oval(10, 230, 110, 330, fill="white")

        self.color.set('R')
        self.canvas.itemconfig(self.oval_red, fill="red")
        
        window.after(0, self.gored)

        window.mainloop()


    def gored(self):
        self.red_state.handle_request(self)
        window.after(time_interval, self.gogreen)
       

    def gogreen(self):
        self.green_state.handle_request(self)
        window.after(time_interval, self.goyellow)


    def goyellow(self):
        self.yellow_state.handle_request(self)
        window.after(time_interval, self.gored)


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

    def handle_request(self, refer):
        print('Wait for turning traffic light to green...')
        self.traffic_light.set_state(self.traffic_light.get_green_light_state())
        refer.canvas.itemconfig(refer.oval_red, fill="red")
        refer.canvas.itemconfig(refer.oval_yellow, fill="white")
        refer.canvas.itemconfig(refer.oval_green, fill="white")

    def __str__(self):
        return 'Traffic light is on red.'


class YellowState(State):

    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def handle_request(self, refer):
        print('Wait for turning traffic light to red...')
        self.traffic_light.set_state(self.traffic_light.get_red_light_state())
        refer.canvas.itemconfig(refer.oval_yellow, fill="yellow")
        refer.canvas.itemconfig(refer.oval_red, fill="white")
        refer.canvas.itemconfig(refer.oval_green, fill="white")

    def __str__(self):
        return 'Traffic light is on yellow.'


class GreenState(State):

    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def handle_request(self, refer):
        print('Wait for turning traffic light to yellow...')
        self.traffic_light.set_state(self.traffic_light.get_yellow_light_state())
        refer.canvas.itemconfig(refer.oval_green, fill="green")
        refer.canvas.itemconfig(refer.oval_red, fill="white")
        refer.canvas.itemconfig(refer.oval_yellow, fill="white")

    def __str__(self):
        return 'Traffic light is on green.'



tr = TrafficLight()
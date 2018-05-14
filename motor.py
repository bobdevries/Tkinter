from tkinter import *
from tkinter import messagebox
# import RPi.GPIO as GPIO # Import the GPIO library
import time 			# Import the time library

# GPIO.setmode(GPIO.BOARD) 

class Test():

	def start(self,dc):
		print("start",dc)

	def ChangeDutyCycle(self,dc):
		print("change dutycycle",dc)

	def stop(self):
		print("stop")

# GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
# pwm = GPIO.PWM(12, 100)   # Initialize PWM on pwmPin 100Hz frequency

pwm = Test()
 
# GPIO.cleanup()                     # resets GPIO ports used back to input mode


class Motor:

	def __init__(self):
		self.dc = 0

	def get_speed(self):
		return self.dc

	def start_motor(self):
		pwm.start(self.dc)

	def stop_motor(self):
		self.dc = 0
		pwm.stop()

	def speed_up(self):
		# global self.speed 
		if self.dc == 100:
			print('maximum speed')
			return
		else:
			self.dc+= 10
		pwm.ChangeDutyCycle(self.dc)
		# print(self.dc)
    # pwm.ChangeDutyCycle(dc)
    # time.sleep(0.05)

	def speed_down(self):
	    # pwm.ChangeDutyCycle(dc)
	    # time.sleep(0.05)
		if self.dc == 0:
			print('minimum speed')
			return
		else:
			self.dc+= -10
		pwm.ChangeDutyCycle(self.dc)
		# print(self.dc)


class Application(Frame):

	motor = Motor()


	def up_button(self):
		motor.speed_up()
		speed  =motor.get_speed()
		self.var.set(speed)
		self.down["state"] = NORMAL
		if speed == 100:
			self.up["state"]=DISABLED
		return

	def down_button(self):
		motor.speed_down()
		speed  =motor.get_speed()
		self.var.set(speed)
		self.up["state"] = NORMAL
		if speed == 0:
			self.down["state"]=DISABLED
		return

	def start_button(self):
		motor.start_motor()
		self.var.set(motor.get_speed())
		self.start["state"] = DISABLED
		self.up["state"] = NORMAL
		self.down["state"] = DISABLED
		self.stop["state"] = NORMAL
		return

	def stop_button(self):
		motor.stop_motor()
		self.var.set(motor.get_speed())
		self.stop["state"] = DISABLED
		self.up["state"] = DISABLED
		self.down["state"] = DISABLED
		self.start["state"] = NORMAL
		return



	# def quit_program(self):
	# 	self.quit
	# 	return

	def callback(self,*args):
		# if motor.get_speed() ==0:
		# 	self.down["state"] =DISABLED
		return

	def createWidgets(self):
		self.var = StringVar()
		self.var.trace("w", self.callback)
		self.var.set(motor.get_speed())
		self.l = Label(root, textvariable = self.var)
		self.l.pack({"side": "right"})

		# self.t = Entry(root, textvariable = self.var)
		# self.t.pack()

		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"]  = "red"
		self.QUIT["command"] =  self.on_quit

		self.QUIT.pack({"side": "left"})
		
		self.start = Button(self)
		self.start["text"] = "Start",
		self.start["activebackground"]  = "green"
		self.start["command"] = self.start_button

		self.start.pack({"side": "right"})


		self.stop = Button(self)
		self.stop["text"] = "Stop",
		self.stop["activebackground"]  = "red"
		self.stop["state"] = DISABLED
		self.stop["command"] = self.stop_button

		self.stop.pack({"side": "right"})

		self.up = Button(self,repeatdelay=500, repeatinterval=100)
		self.up["text"] = "Up",
		self.up["state"] = DISABLED
		self.up["command"] = self.up_button
		self.up.bind("<ButtonRelease>", self.on_release)
		# lambda: speed_up(dc)

		self.up.pack({"side": "left"})

		self.down = Button(self,repeatdelay=500, repeatinterval=100)
		self.down["text"] = "Down",
		self.down["state"] = DISABLED
		self.down["command"] = self.down_button
		self.down.pack({"side": "left"})
		self.down.bind("<ButtonRelease>", self.on_release)

	def on_release(self,event):
		return
		# speed = motor.get_speed()
		# if speed == 0:
		# 	self.down["state"]=DISABLED
		# elif speed == 100:
		# 	self.up["state"]=DISABLED
		# print("button was released")

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		root.protocol("WM_DELETE_WINDOW", self.on_exit)

	def on_quit(self):
		if messagebox.askyesno("Exit", "Do you want to quit the application?"):
			# GPIO.cleanup()
			root.quit()


	def on_exit(self):
		# """When you click to exit, this function is called"""
		if messagebox.askyesno("Exit", "Do you want to quit the application?"):
			# GPIO.cleanup()
			root.destroy()


root = Tk()
motor = Motor()

app = Application(master=root)
app.mainloop()
root.destroy()




def main():
	return

if __name__ == '__main__':
    main()
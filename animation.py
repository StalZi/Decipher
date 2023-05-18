from customtkinter import CTkFrame

class SlidePanel(CTkFrame):
	
	def __init__(self, parent, start_pos, end_pos):
		super().__init__(master = parent)

		# general attributes 
		self.start_pos = start_pos + 0.04
		self.end_pos = end_pos - 0.03

		# animation logic
		self.pos = self.start_pos
		self.in_start_pos = True

		# layout
		self.place(relx = self.start_pos, rely = 0.165, relheight = 1.0)
		

	def animate(self):
		
		if self.in_start_pos:
			self.animate_forward()
			
		else:
			self.animate_backwards()
			

	def animate_forward(self):
		
		if self.pos < self.end_pos and self.in_start_pos:
			self.pos += 0.01
			self.place(relx = self.pos, rely = 0.165, relheight = 1.0)
			self.after(10, self.animate_forward)
			
		else:
			self.in_start_pos = False
			

	def animate_backwards(self):
		
		if self.pos > self.start_pos and not self.in_start_pos:
			self.pos -= 0.001
			self.place(relx = self.pos, rely = 0.165, relheight = 1.0)
			self.after(10, self.animate_backwards)
			
		else:
			self.in_start_pos = True
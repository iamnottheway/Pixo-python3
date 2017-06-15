
import random
from tkinter import *
from colors import COLORS
from MoveWindow import MovableWindow

BG_COLOR = "#24272b"

class ColorPalette():

	def __init__(self,master):
		self.master = master 
		self.child_win = Toplevel(self.master)
		self.child_win.geometry("300x320+300+200")
		self.child_win.config(bg=BG_COLOR)
		self.child_win.resizable(0,0)
		self.child_win.title("color pallette")
		self.child_win.overrideredirect(1)
		# default color
		self.move_window_canvas = MovableWindow(self.child_win)
		self.def_color = "red"
		self.ColorPaletteCanvas = Canvas(self.child_win,width = 210,height = 220,bg = 'white',cursor = 'tcross')
		self.ColorPaletteCanvas.grid(row = 1,column=1,padx = 10,pady = 10)
				# colors inside the palette
		self.x_pos = 0
		self.y_pos = 0
				# final x coord of the canvas is 200
				# and y coord is 100. -20 from them
		for c in COLORS:
			self.colorsInside = self.ColorPaletteCanvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+10,self.y_pos+10,fill = c,tags=("{0}".format(c)))
			#showing all the colors on the screen
			self.x_pos += 10
			if self.x_pos > 200:
				self.y_pos += 10
				self.x_pos = 0
		# current is a keyword. It points to the current object. Alternative: CURRENT
		# gets the current clicked color from the palette
		self.ColorPaletteCanvas.tag_bind("current",'<Button-1>',self.get_color)

		self.col_can = Canvas(self.child_win,width = 30,height = 30,bg = self.def_color )
		self.col_can.grid(row = 2,column=1,padx = 100,pady = 10,sticky = W)
		self.col_lab = Label(self.child_win,text = self.def_color,bg = BG_COLOR,fg = "#fff")
		self.col_lab.grid(row = 2,column=1,padx = 50,pady = 3,sticky = E)

	def filter_colornames(self,name):
		self.name = name
		self.f_name = ""
		for x in range(0,len(self.name)):
			if self.name[x] == " ":
				break 
			self.f_name += self.name[x]
		return self.f_name


	def get_color(self,*args):
		self.current_color = self.ColorPaletteCanvas.itemcget("current","tags")
		self.col_can.config(bg = self.filter_colornames(self.current_color))
		self.col_lab.config(text=self.filter_colornames(self.current_color))
		self.child_win.update()
		print(self.filter_colornames(self.current_color))
		return self.filter_colornames(self.current_color)
	#	except Exception as e:
	#		print(e)
	

#root = Tk()
#win = ColorPalette(root)
#root.mainloop()
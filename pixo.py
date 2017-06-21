# pixel art editor

from tkinter import *
from color_palette import ColorPalette


BG_COLOR = "#24272b"
# icon author creds
# <div>Icons made by <a href="http://www.flaticon.com/authors/dinosoftlabs" title="DinosoftLabs">DinosoftLabs</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
class Pixo():
	def __init__(self,master):
		# window configs

		self.master = master
		self.size = [650,450]
		self.master.title("Pixo")
		self.master.geometry("{0}x{1}+400+200".format(self.size[0],self.size[1]))
		self.master.resizable(0,0)
		self.master.config(bg=BG_COLOR)

		self.seletected_color = "#3a3"

		# color picker frame
		self.color_picker_frame = Canvas(self.master,width = self.size[0]-20,height = 30,bg = "#333",highlightthickness=0)
		self.color_picker_frame.grid(row = 0,column = 1,padx = 10,pady = 10,sticky = W)

		self.colors = ["#ea2525","#eae624","#24ea4b","#f44192","#426bf4","#ffffff","#000","#3d5","#808080","#008000","#00FFFF",\
		"#008080","#0000FF"]
		n_cols = 0
		x_pos = 0
		y_pos = 0
#		for x in self.colors:
#			self.color_picker_frame.create_rectangle(x_pos,y_pos,x_pos+20,y_pos+20,fill = x,tags = "{0}".format(x))
#			if x_pos > 500:
#				y_pos += 20
#				x_pos = 0
		self.color_pick_btn = Button(self.color_picker_frame,width = 1,height = 1,bd = 0,command = self.pick_color)
		self.color_pick_btn.grid(row = 1,column = 10)

		#self.color_picker_frame.tag_bind("current",'<Button-1>',self.get_color)
		# draw canvas
		self.draw_canvas = Canvas(self.master,width = self.size[0]-20,height=self.size[1]-90,bg="#fff")
		self.draw_canvas.grid(row = 1,column = 1,padx = 10,pady =10)
		# make the grid
		x_gridP = 0
		y_gridP = 0
		for x in range(2500):
			self.draw_canvas.create_rectangle(x_gridP,y_gridP,x_gridP+10,y_gridP+10,fill = '#fff',outline="gray21",\
				tags = "color-grid-{0}".format(x))
			x_gridP += 10
			if x_gridP > self.size[0]-20:
				y_gridP += 10
				x_gridP = 0

		self.draw_canvas.tag_bind("current",'<Button-1>',self.paint_block)

	def paint_block(self,*args):
		# fill the block when clicked on it
		self.draw_canvas.itemconfig(CURRENT,fill = self.seletected_color)

	def pick_color(self):
		# get the selected color name from the canvas
		self.color_picker = ColorPalette(self.master)
		self.seletected_color = self.color_picker.get_color()
		# update the previous color
		self.master.update()

		


app = Tk()
win = Pixo(app)
app.mainloop()

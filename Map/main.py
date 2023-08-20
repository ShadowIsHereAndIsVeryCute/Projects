import customtkinter as ctk
from settings import *
import tkintermapview
from geopy.geocoders import Nominatim
from translate import Translator
class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		ctk.set_appearance_mode('light')
		self.geometry('1200x800=100+50')
		self.minsize(800,600)
		self.title('Map')
		self.iconbitmap('map.ico')

		self.input_string = ctk.StringVar()

		self.columnconfigure(0, weight=2, uniform='a')
		self.columnconfigure(1, weight=8, uniform='a')
		self.rowconfigure(0, weight =1, uniform= 'a')

		self.map_widget = MapWidget(self, self.input_string, self.submit_location)
		self.mainloop()

	def submit_location(self,event):
		geolocator = Nominatim(user_agent = 'my-user')
		location = geolocator.geocode(self.input_string.get())


		if location == None:
			self.map_widget.location_entry.error_animation()
		else:
			self.map_widget.set_address(location.address)

			self.input_string.set('')




class MapWidget(tkintermapview.TkinterMapView):
	def __init__(self,parent, input_string, submit_location):
		super().__init__(parent)
		self.grid(row = 0, column = 1, sticky = 'nesw')
		#self.set_tile_server(TERRAIN_URL)

		self.location_entry = LocEntry(self, input_string, submit_location)


class LocEntry(ctk.CTkEntry):
	def __init__(self,parent,input_string, submit_location):
		self.color_index = 15
		self.invert_index = 0
		self.error = False
		color = COLOR_RANGE[self.color_index]
		super().__init__(parent,
						 textvariable= input_string,
						 corner_radius= 0,
						 border_width= 4,
						 fg_color= ENTRY_BG,
						 text_color= TEXT_COLOR,
						 font = ctk.CTkFont(family= TEXT_FONT, size= TEXT_SIZE),
						 border_color= f'#F{color}{color}')
		self.place(relx = 0.5, rely= 0.95, anchor = 'center')

		self.bind('<Return>', submit_location)

		input_string.trace('w', self.remove_error)
	def error_animation(self):
		self.error = True
		if self.color_index > 0 and self.invert_index < 14:
			self.color_index -=1
			self.invert_index += 1
			border_color = f'#F{COLOR_RANGE[self.color_index]}{COLOR_RANGE[self.color_index]}'
			text_color = f'#{COLOR_RANGE[self.invert_index]}00'
			self.configure(border_color = border_color, text_color= text_color)
			self.after(40, self.error_animation)
	def remove_error(self, *args):
		if self.error:
			self.configure(border_color= ENTRY_BG, text_color= TEXT_COLOR)
			self.color_index = 15
			self.invert_index = 0

App()


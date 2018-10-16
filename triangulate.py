import kivy
kivy.require("1.10.1")

import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TrigBoxLayout(BoxLayout):
	"""docstring for BoxLayout"""
	# def __init__(self, Northing1, Northing2, Easting1, Easting2, Angle1, Angle2):
	# 	super(TrigBoxLayout, self).__init__()
	# 	self.N1.text = Northing1
	# 	self.N2.text = Northing2
	# 	self.E1.text = Easting1
	# 	self.E2.text = Easting2
	# 	self.A1.text = Angle1
	# 	self.A2.text = Angle2

	def computeNorthing(self):
		N1 = int(self.ids.N1.text)
		N2 = int(self.ids.N2.text)
		E1 = int(self.ids.E1.text)
		E2 = int(self.ids.E2.text)
		A1 = int(self.ids.A1.text)
		A2 = int(self.ids.A2.text)

		Northing = ((E1 - E2) + N2*(math.tan(math.radians(A2))) - N1*(math.tan(math.radians(A1))))/((math.tan(math.radians(A2))) - (math.tan(math.radians(A1))))
		self.ids.N.text = str(Northing) 
	   
	def computeEasting(self):
		N1 = int(self.ids.N1.text)
		N2 = int(self.ids.N2.text)
		E1 = int(self.ids.E1.text)
		E2 = int(self.ids.E2.text)
		A1 = int(self.ids.A1.text)
		A2 = int(self.ids.A2.text)

		Easting  = ((N2 - N1) + E1/(math.tan(math.radians(A1))) - E2/(math.tan(math.radians(A2))))/(1/(math.tan(math.radians(A1))) -1/(math.tan(math.radians(A2))))
		self.ids.E.text = str(Easting)

			
class TriangulateApp(App):
	"""docstring for ClassName"""
	def build(self):
		return TrigBoxLayout()

trig = TriangulateApp()
trig.run()
		
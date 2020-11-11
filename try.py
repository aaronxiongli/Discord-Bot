import os
class inter():
	def __init__(self,code):
		self.code=code
		self.splitss()
	def splitss(self):
		self.code_split=self.code.split("/")
		self.writee()
	def writee(self):
		with open("lol.py",'w+') as l:
			l.truncate(0)
		with open("lol.py",'a+') as f:
			for i in range(0,len(self.code_split)):
				f.write(self.code_split[i]+"\n")
				

